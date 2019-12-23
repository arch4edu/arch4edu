# Maintainer: Daniel Maslowski <info@orangecms.org>

pkgname=python-conda
_name=${pkgname#python-}
pkgver=4.8.0
pkgrel=1
pkgdesc="OS-agnostic, system-level binary package manager and ecosystem"
arch=('any')
url="http://conda.pydata.org/docs/"
license=('BSD')
depends=(
  'python'
  'python-conda-package-handling'
  'python-pycosat>=0.6.3'
  'python-requests>=2.12.4'
  'python-ruamel-yaml'
  'python-libarchive-c'
  'python-tqdm'
)
makedepends=('python-setuptools')
optdepends=(
  'python-conda-build: to use the conda build command'
)
provides=('python-conda' 'python-conda-env')
options=(!emptydirs)
source=(
  $_name-$pkgver.tar.gz::https://github.com/$_name/$_name/archive/$pkgver.tar.gz
)
sha512sums=('c85ea7b051171479ee387fb6d54204ab59489521ac822797c4dc7b5be120c4b8a6844eb7c36ec85d3238dbb5a1525e8c5371df0d2b478d26e25d2bac5e26a07e')

prepare() {
  cd "$srcdir/${_name}-$pkgver"
  echo $pkgver > conda/.version
  sed -i "s/package_files('conda\/shell') + //" setup.py
  sed -i 's/$_CONDA_ROOT//' conda/shell/bin/{de,}activate
  sed -i 's/env python/python3/' conda/shell/bin/conda
  sed "s/conda.cli/conda_env.cli.main/" conda/shell/bin/conda > conda/shell/bin/conda-env
  echo 'set -l CONDA_EXE /usr/bin/conda' | cat - conda/shell/etc/fish/conf.d/conda.fish > conda.fish
  echo 'set _CONDA_EXE=/usr/bin/conda' | cat - conda/shell/etc/profile.d/conda.csh > conda.csh
  echo 'export CONDA_EXE=/usr/bin/conda' | cat - conda/shell/etc/profile.d/conda.sh > conda.sh
}

build() {
  cd "$srcdir/${_name}-$pkgver"
  python setup.py clean --all
  python setup.py build
}

package() {
  cd "$srcdir/${_name}-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
  for _bin in $(ls conda/shell/bin); do
    install -Dm 655 conda/shell/bin/$_bin $pkgdir/usr/bin/$_bin
  done
  install -Dm 644 conda.fish $pkgdir/usr/share/fish/functions/conda.fish
  install -Dm 644 conda.csh $pkgdir/etc/profile.d/conda.csh
  install -Dm 644 conda.sh $pkgdir/etc/profile.d/conda.sh
  install -Dm 644 LICENSE.txt $pkgdir/usr/share/licenses/${pkgname}/LICENSE.txt
}

# vim:set ts=2 sw=2 et:
