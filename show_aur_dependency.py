#!/usr/bin/env python3
"""
简易版：显示包的 AUR 依赖
- 不维护 pacman 数据库，直接读系统 pacman sync db
- 无额外参数
- 只列出 AUR 依赖
"""

import subprocess
import requests
import sys
import logging
import tarfile
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger()

def load_pacman_db():
    """从系统 pacman sync 数据库加载包名和 provides 映射，记录仓库来源（仅 core, extra, arch4edu）"""
    packages = set()
    provides = {}
    pkg_to_repo = {}  # 包名 → 仓库名
    
    # 同步数据库路径
    sync_dir = Path('/var/lib/pacman/sync')
    
    if not sync_dir.exists():
        logger.error('Cannot find pacman sync directory')
        sys.exit(1)
    
    logger.info(f'Reading pacman sync db from {sync_dir}')
    
    # 只读取 core, extra, arch4edu 仓库
    for repo in ['core', 'extra', 'arch4edu']:
        db_file = sync_dir / f'{repo}.db'
        if not db_file.exists():
            logger.warning(f'{db_file} not found, skipping')
            continue
        
        try:
            with tarfile.open(db_file, 'r:gz') as tar:
                for member in tar.getmembers():
                    if not member.name.endswith('/desc'):
                        continue
                    f = tar.extractfile(member)
                    if not f:
                        continue
                    try:
                        name = None
                        in_provides = False
                        for raw_line in f:
                            line = raw_line.decode('utf-8', errors='ignore').strip()
                            if line == '%NAME%':
                                name_raw = f.readline()
                                if name_raw:
                                    name = name_raw.decode('utf-8', errors='ignore').strip()
                                    if name:
                                        packages.add(name)
                                        pkg_to_repo[name] = repo
                            elif line == '%PROVIDES%':
                                in_provides = True
                            elif in_provides:
                                if line.startswith('%'):
                                    break
                                if line:
                                    pname = line.split('=')[0].split('<')[0].split('>')[0].strip()
                                    if pname and name:
                                        provides[pname] = name
                                        # provides 也记录仓库来源
                                        if pname not in pkg_to_repo:
                                            pkg_to_repo[pname] = repo
                    finally:
                        f.close()
        except Exception as e:
            logger.debug(f'Failed to read {db_file}: {e}')
    
    logger.info(f'Loaded {len(packages)} packages and {len(provides)} provides from core+extra+arch4edu')
    return packages, provides, pkg_to_repo

def get_aur_info(packages):
    """从 AUR RPC 查询包信息"""
    if not packages:
        return {}
    
    AUR_URL = 'https://aur.archlinux.org/rpc/'
    params = [('v', '5'), ('type', 'info')]
    params.extend(('arg[]', pkg) for pkg in packages)
    
    try:
        res = requests.get(AUR_URL, params=params, timeout=30)
        data = res.json()
        if data['type'] == 'error':
            logger.error(f'AUR API error: {data.get("error", "Unknown error")}')
            sys.exit(1)
        results = {r['Name']: r for r in data['results']}
        logger.info(f'Got AUR info for {len(results)} packages')
        return results
    except Exception as e:
        logger.error(f'Failed to query AUR: {e}')
        sys.exit(1)

def resolve_aur_dependencies(pkgname, pacman_packages, provides, pkg_to_repo, aur_cache=None):
    """解析包的依赖（仅直接依赖，不递归），标注来源"""
    if aur_cache is None:
        aur_cache = {}
    
    # 检查目标包是否在 AUR 中
    if pkgname not in aur_cache:
        info = get_aur_info([pkgname])
        if pkgname not in info:
            logger.warning(f'Package {pkgname} not found in AUR')
            return []
        aur_cache.update(info)
    
    info = aur_cache[pkgname]
    
    # 收集直接依赖
    depends = info.get('Depends', [])
    makedepends = info.get('MakeDepends', [])
    if 'CheckDepends' in info:
        makedepends += info['CheckDepends']
    
    all_deps = depends + makedepends
    deps_with_source = []
    
    for dep in all_deps:
        # 提取包名（去掉版本限制）
        pkg = dep.split('<')[0].split('>')[0].split('=')[0].strip()
        if not pkg:
            continue
        
        # 处理 provides 映射
        pkg = provides.get(pkg, pkg)
        
        # 判断包来源
        if pkg in pacman_packages:
            repo = pkg_to_repo.get(pkg, 'unknown')
            if repo in ['core', 'extra']:
                # 核心/官方仓库，跳过
                continue
            else:
                # 第三方仓库，显示
                deps_with_source.append((pkg, repo, 'repo'))
        else:
            # 不在任何 pacman 仓库中 → AUR
            deps_with_source.append((pkg, 'AUR', 'aur'))
    
    # 去重并排序（按包名）
    seen = set()
    unique_deps = []
    for pkg, source, source_type in sorted(deps_with_source, key=lambda x: x[0]):
        if pkg not in seen:
            seen.add(pkg)
            unique_deps.append((pkg, source))
    
    return unique_deps

def main():
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <package-name>')
        sys.exit(1)
    
    pkgname = sys.argv[1]
    
    # 加载 pacman 同步数据库（所有仓库）
    pacman_pkgs, provides, pkg_to_repo = load_pacman_db()
    
    # 解析 AUR 依赖
    aur_deps = resolve_aur_dependencies(pkgname, pacman_pkgs, provides, pkg_to_repo)
    
    # 输出结果
    print(f'\nAUR dependencies for {pkgname}:')
    if aur_deps:
        for pkg, repo in aur_deps:
            print(f'  - {pkg} (from {repo})')
        print(f'\nTotal: {len(aur_deps)} AUR package(s)')
    else:
        print('  No AUR dependencies found (all dependencies are in official repos)')

if __name__ == '__main__':
    main()