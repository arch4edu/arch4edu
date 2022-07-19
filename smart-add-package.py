#!/bin/python
import os
import sys
import logging
import requests
import shutil
import subprocess
import yaml
from pathlib import Path

def run(command, **kwargs):
    return subprocess.run(command, check=True, **kwargs)

remove = os.remove
move = shutil.move
rmtree = shutil.rmtree

def symlink(source, target):
    try:
        os.symlink(source, target)
    except FileExistsError:
        os.remove(target)
        os.symlink(source, target)

def load_pacman_packages():
    run(['sudo', 'pacman', '-Sy'])
    results = set()
    for repository in ['core', 'extra', 'community', 'arch4edu']:
    #for repository in ['core', 'extra', 'community']:
        packages = run(['sudo', 'pacman', '-Slq', repository], capture_output=True)
        results.update(packages.stdout.decode('utf-8').split('\n')[:-1])
    return results

def read_aur_info(packages):
    logger.info('Reading AUR package information for %s', packages)
    AUR_URL = 'https://aur.archlinux.org/rpc/'
    params = [('v', '5'), ('type', 'info')]
    params.extend(('arg[]', i) for i in packages)
    res = requests.get(AUR_URL, params=params)
    data = res.json()
    results = {r['Name']: r for r in data['results']}
    return results

def read_provides(package):
    os.environ['LANG'] = 'C'
    info = run(['sudo', 'pacman', '-Si', package], capture_output=True)
    info = info.stdout.decode('utf-8').split('\n')
    provides = [line for line in info if line.startswith('Provides')][0]
    provides = provides.split(':')[-1].split(' ')
    provides = [i.split('=')[0] for i in provides if len(i) > 0]
    results = {}
    for i in provides:
        results[i] = package
    return results

provides = {}
provides.update(read_provides('r'))
provides.update(read_provides('fuse2'))
provides.update(read_provides('libjpeg-turbo'))
provides.update(read_provides('ttf-dejavu'))

if __name__ == '__main__':
    from tornado.log import enable_pretty_logging
    from tornado.options import options

    options.logging = 'debug'
    logger = logging.getLogger()
    enable_pretty_logging(options=options, logger=logger)

    pacman_db = load_pacman_packages()

    unresolved = [sys.argv[1]]
    resolved = {}
    reversed_depends = {}
    while len(unresolved) > 0:
        aur_info = read_aur_info(unresolved)
        _unresolved = set()
        for package in unresolved:
            if not package in aur_info:
                logger.error('Cannot find %s in AUR.', package)
                for _package, info in resolved.items():
                    if 'Depends' in info and package in info['Depends']:
                        logger.error('%s is required by %s', package, _package)
                    if 'MakeDepends' in info and package in info['MakeDepends']:
                        logger.error('%s is required by %s', package, _package)
                sys.exit(1)

            aur_info[package]['Depends'] = [] if not 'Depends' in aur_info[package] else aur_info[package]['Depends']
            aur_info[package]['Depends'] = [i.split('>')[0].split('=')[0] for i in aur_info[package]['Depends']]
            aur_info[package]['Depends'] = [provides[i] if i in provides else i for i in aur_info[package]['Depends']]
            aur_info[package]['Depends'] = [i for i in aur_info[package]['Depends'] if not i in pacman_db]
            _unresolved.update([i for i in aur_info[package]['Depends'] if not i in resolved])

            aur_info[package]['MakeDepends'] = [] if not 'MakeDepends' in aur_info[package] else aur_info[package]['MakeDepends']
            if 'CheckDepends' in aur_info[package]:
                    aur_info[package]['MakeDepends'] += aur_info[package]['CheckDepends']
            aur_info[package]['MakeDepends'] = [i.split('>')[0].split('=')[0] for i in aur_info[package]['MakeDepends']]
            aur_info[package]['MakeDepends'] = [provides[i] if i in provides else i for i in aur_info[package]['MakeDepends']]
            aur_info[package]['MakeDepends'] = [i for i in aur_info[package]['MakeDepends'] if not i in pacman_db and not i in aur_info[package]['Depends']]
            _unresolved.update([i for i in aur_info[package]['MakeDepends'] if not i in resolved])

            resolved[package] = aur_info[package]
            logger.info('Resolved %s', package)
        unresolved = list(_unresolved)
    logger.info('Resolved %d packages', len(resolved))
    logger.debug(resolved['r-httpuv'])

    path = Path(sys.argv[2])
    path.mkdir(exist_ok=True)
    for package, info in resolved.items():
        pkgbase = path / info['PackageBase']
        if (pkgbase / 'cactus.yaml').exists():
            continue
        pkgbase.mkdir(exist_ok=True)
        template = 'template/x86_64-simple.yaml'
        if len(info['Depends']) + len(info['MakeDepends']) == 0:
            symlink('../' * (sys.argv[2].count('/') + 2) + template, pkgbase / 'cactus.yaml')
            logger.info('Added %s with %s', package, template)
        else:
            with open(template) as f:
                lines = f.readlines()
            with open(pkgbase / 'cactus.yaml', 'w') as f:
                for line in lines:
                    if line.startswith('build_prefix'):
                        if len(info['Depends']) > 0:
                            f.write('depends:\n')
                        for i in info['Depends']:
                            if resolved[i]['PackageBase'] == i:
                                f.write(f'  - {sys.argv[2]}/{i}\n')
                            else:
                                f.write(f'  - {sys.argv[2]}/{resolved[i]["PackageBase"]}: {i}\n')
                        if len(info['MakeDepends']) > 0:
                            f.write('makedepends:\n')
                        for i in info['MakeDepends']:
                            if resolved[i]['PackageBase'] == i:
                                f.write(f'  - {sys.argv[2]}/{i}\n')
                            else:
                                f.write(f'  - {sys.argv[2]}/{resolved[i]["PackageBase"]}: {i}\n')
                    f.write(line)
            logger.info('Added %s', package)
