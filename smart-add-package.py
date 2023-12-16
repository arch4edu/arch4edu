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
    #for repository in ['core', 'extra', 'arch4edu']:
    for repository in ['core', 'extra']:
        packages = run(['sudo', 'pacman', '-Slq', repository], capture_output=True)
        results.update(packages.stdout.decode('utf-8').split('\n')[:-1])
    return results

def load_pkgbases():
    pkgbases = {}
    for i in Path('.').rglob('cactus.yaml'):
        pkgbase = i.parent.name
        pkgbases[pkgbase] = str(i.parent)
    return pkgbases

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

def load_provides():
    provides = {}
    provides.update(read_provides('fuse2'))
    provides.update(read_provides('libjpeg-turbo'))
    provides.update(read_provides('ttf-dejavu'))
    provides.update(read_provides('ruby-ronn-ng'))
    provides.update(read_provides('libtool'))
    provides.update(read_provides('util-linux-libs'))
    provides.update(read_provides('pkgconf'))
    provides.update(read_provides('gtest'))
    provides.update(read_provides('dbus-python'))
    provides.update(read_provides('jdk-openjdk'))
    provides.update(read_provides('jre-openjdk'))
    return provides

if __name__ == '__main__':
    import argparse
    from tornado.log import enable_pretty_logging
    from tornado.options import options

    parser = argparse.ArgumentParser()
    parser.add_argument('--template', '-t', default='template/x86_64-simple.yaml', help='the template used to create cactus.yaml (default: template/x86_64-simple.yaml)')
    #parser.add_argument('--repository', default='.', help='path to the repository (default: current directory)')
    parser.add_argument('--provides', '-p', action='append', help='read the provides of a package')
    parser.add_argument('--nocheck', action="store_true", help='disable check and ignore checkdepends (please remember to also use the nocheck template)')
    parser.add_argument('package', help='the package to add (eg: yay)')
    parser.add_argument('directory', help='the output directory (eg: x86_64, x86_64/directory)')
    args = parser.parse_args()

    options.logging = 'debug'
    logger = logging.getLogger()
    enable_pretty_logging(options=options, logger=logger)

    directory = Path(args.directory)
    directory.mkdir(exist_ok=True)
    template = args.template

    pacman_db = load_pacman_packages()
    pkgbases = load_pkgbases()
    provides = load_provides()
    if not args.provides is None:
        for i in args.provides:
            provides.update(read_provides(i))

    unresolved = [args.package]
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
            if not args.nocheck and 'CheckDepends' in aur_info[package]:
                aur_info[package]['MakeDepends'] += aur_info[package]['CheckDepends']
            aur_info[package]['MakeDepends'] = [i.split('>')[0].split('=')[0] for i in aur_info[package]['MakeDepends']]
            aur_info[package]['MakeDepends'] = [provides[i] if i in provides else i for i in aur_info[package]['MakeDepends']]
            aur_info[package]['MakeDepends'] = [i for i in aur_info[package]['MakeDepends'] if not i in pacman_db and not i in aur_info[package]['Depends']]
            _unresolved.update([i for i in aur_info[package]['MakeDepends'] if not i in resolved])

            resolved[package] = aur_info[package]
            logger.info('Resolved %s', package)
        unresolved = list(_unresolved)
    logger.info('Resolved %d packages', len(resolved))

    for package, info in reversed(resolved.items()):
        pkgbase = info['PackageBase']
        if pkgbase in pkgbases and pkgbase != args.package:
            continue

        pkgbase = directory / pkgbase
        pkgbase.mkdir(exist_ok=True)
        config = pkgbase / 'cactus.yaml'
        config.unlink(missing_ok=True)

        if len(info['Depends']) + len(info['MakeDepends']) == 0:
            symlink('../' * (len(directory.parents) + 1) + template, config)
            logger.info('Added %s with %s', package, template)
            pkgbases[pkgbase.name] = str(pkgbase)
        else:
            with open(template) as f:
                lines = f.readlines()

            with open(config, 'w') as f:
                for line in lines:
                    if line.startswith('build_prefix'):
                        if len(info['Depends']) > 0:
                            f.write('depends:\n')
                        for i in info['Depends']:
                            _pkgbase = resolved[i]['PackageBase']
                            _pkgbase = pkgbases[_pkgbase] if _pkgbase in pkgbases else str(directory / _pkgbase)
                            if resolved[i]['PackageBase'] == i:
                                f.write(f'  - {_pkgbase}\n')
                            else:
                                f.write(f'  - {_pkgbase}: {i}\n')
                        if len(info['MakeDepends']) > 0:
                            f.write('makedepends:\n')
                        for i in info['MakeDepends']:
                            _pkgbase = resolved[i]['PackageBase']
                            _pkgbase = pkgbases[_pkgbase] if _pkgbase in pkgbases else str(directory / _pkgbase)
                            if resolved[i]['PackageBase'] == i:
                                f.write(f'  - {_pkgbase}\n')
                            else:
                                f.write(f'  - {_pkgbase}: {i}\n')
                    f.write(line)
            pkgbases[pkgbase.name] = str(pkgbase)
            logger.info('Added %s', package)
