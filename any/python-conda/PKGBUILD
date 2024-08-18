# Maintainer: Brian Thompson <brianrobt@pm.me>
# Contributor: Daniel Maslowski <info@orangecms.org>
# Contributor: Ke Liu <specter119@gmail.com>

pkgname=python-conda
_name=${pkgname#python-}
pkgver=24.7.1
pkgrel=4
pkgdesc="OS-agnostic, system-level binary package manager and ecosystem https://conda.io"
arch=('any')
url="https://github.com/conda/conda"
license=('BSD-3-Clause')
depends=(
  'python>=3.7'
  'python-archspec'
  'python-boltons'
  'python-boto3'
  'python-botocore'
  'python-conda-package-handling'
  'python-libmamba'
  'python-pluggy>=1.0.0'
  'python-pycosat>=0.6.3'
  'python-requests>=2.20.1'
  'python-ruamel-yaml>=0.11.14'
  'python-tqdm'
)
checkdepends=(
  'python-pytest'
  'python-pytest-mock'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-hatchling'
  'python-hatch-vcs'
  'python-wheel'
)
provides=('python-conda' 'python-conda-env')
options=(!emptydirs)
backup=(etc/conda/condarc)
source=(
  $_name-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz
)
sha512sums=('8fbd8e868a9ac0a73c0d940a393ebbf25f16d1b82ca6c59691e148dbb20c7d4767794fae72cd9a84f071714065e80f8f859f629a239e75feaf43c5d570625a59')

prepare() {
  cd $srcdir/${_name}-$pkgver
  echo $pkgver > conda/.version
  # sed -i "s/package_files(\'conda\/shell') + //" setup.py
  # sed -i 's/$_CONDA_ROOT//' conda/shell/bin/{de,}activate
  sed -i 's/env python/python3/' conda/shell/bin/conda
  sed -i '3s/^/set _CONDA_EXE=\/usr\/bin\/conda\n/' conda/shell/etc/profile.d/conda.csh
  sed -i '3s/^/export CONDA_EXE=\/usr\/bin\/conda\n/' conda/shell/etc/profile.d/conda.sh
  sed -i '8s/^/set -l CONDA_EXE \/usr\/bin\/conda\n/' conda/shell/etc/fish/conf.d/conda.fish
  # BEGIN Patch conda binary
  sed -i 's/ import/.main import/'  conda/shell/bin/conda
  sed -i 's/path.main/path/'  conda/shell/bin/conda
  sed -i 's/from conda.deprecations/# from conda.deprecations/'  conda/shell/bin/conda
  sed -i 's/deprecated.module/# deprecated.module/'  conda/shell/bin/conda
  sed -i 's/"24/# "24/g'  conda/shell/bin/conda
  sed -i 's/addendum/# addendum/g'  conda/shell/bin/conda
  sed -i 's/  )/#  )/'  conda/shell/bin/conda
  # END
  # echo 'set -l CONDA_EXE /usr/bin/conda' | cat - conda/shell/etc/fish/conf.d/conda.fish > conda.fish
  # echo 'set _CONDA_EXE=/usr/bin/conda' | cat - conda/shell/etc/profile.d/conda.csh > conda.csh
  # echo 'export CONDA_EXE=/usr/bin/conda' | cat - conda/shell/etc/profile.d/conda.sh > conda.sh
  echo -e 'envs_dirs:\n  - ~/.conda/envs\npkgs_dirs:\n  - ~/.conda/pkgs' > condarc
}

build() {
  cd $srcdir/${_name}-$pkgver
  python -m build --wheel --no-isolation
}

package() {
  cd $srcdir/${_name}-$pkgver
  python -m installer --destdir $pkgdir $srcdir/${_name}-$pkgver/dist/${_name}-$pkgver-*.whl
  rm -f conda/shell/bin/{,de}activate
  # for _bin in $(ls conda/shell/bin); do
  #   install -Dm 655 conda/shell/bin/$_bin $pkgdir/usr/bin/$_bin
  # done
  # install -Dm 644 conda.fish $pkgdir/usr/share/fish/functions/conda.fish
  # install -Dm 644 conda.csh $pkgdir/etc/profile.d/conda.csh
  # install -Dm 644 conda.sh $pkgdir/etc/profile.d/conda.sh
  mkdir -p $pkgdir/{usr/share/fish/functions,etc/profile.d}
  _dir_sitepackage=$(python -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')
  ln -s ${_dir_sitepackage}/conda/shell/etc/fish/conf.d/conda.fish $pkgdir/usr/share/fish/functions/conda.fish
  ln -s ${_dir_sitepackage}/conda/shell/etc/profile.d/conda.csh $pkgdir/etc/profile.d/conda.csh
  ln -s ${_dir_sitepackage}/conda/shell/etc/profile.d/conda.sh $pkgdir/etc/profile.d/conda.sh
  # BEGIN Install patched conda binary
  rm -f $pkgdir/usr/bin/conda
  install -Dm 755 conda/shell/bin/conda $pkgdir/usr/bin/conda
  # END
  install -Dm 644 condarc $pkgdir/etc/conda/condarc
  install -Dm 644 LICENSE $pkgdir/usr/share/licenses/${pkgname}/LICENSE
}

# vim:set ts=2 sw=2 et:
