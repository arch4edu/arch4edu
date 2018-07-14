# Maintainer: Daniel Maslowski <info@orangecms.org>

_pyname=conda
pkgname=python-conda
pkgver=4.5.8
pkgrel=1
pkgdesc="OS-agnostic, system-level binary package manager and ecosystem"
arch=('any')
url="http://conda.pydata.org/docs/"
license=('BSD')
depends=('python' 'python-pycosat>=0.6.1' 'python-requests' 'python-ruamel-yaml')
optdepends=(
  'python-conda-build: to use the conda build command'
)
provides=('python-conda' 'python-conda-env')
options=(!emptydirs)
source=(
  https://github.com/$_pyname/$_pyname/archive/$pkgver.tar.gz
)
sha512sums=('33c0ace75b44b86e4f086e580f99fada75a175147905f4d4877b8e13fda156e7601b040ee65ec1f7d058780a7ea830db73fb28b6726a9c5c6f4b32e06bc09505')

prepare() {
  cd "$srcdir/${_pyname}-$pkgver"
  sed -i 's/$_CONDA_ROOT//' conda/shell/bin/{de,}activate
  sed -i 's/env python/python3/' conda/shell/bin/conda
}

package() {
  cd "$srcdir/${_pyname}-$pkgver"
  echo $pkgver > conda/.version
  python utils/setup-testing.py install --root="$pkgdir/" --optimize=1
  sed "s/conda.cli/conda_env.cli.main/" conda/shell/bin/conda > conda/shell/bin/conda-env
  install -Dm 655 conda/shell/bin/activate $pkgdir/usr/bin/activate
  install -Dm 655 conda/shell/bin/conda $pkgdir/usr/bin/conda
  install -Dm 655 conda/shell/bin/conda-env $pkgdir/usr/bin/conda-env
  install -Dm 655 conda/shell/bin/deactivate $pkgdir/usr/bin/deactivate
  echo 'set _CONDA_EXE /usr/bin/conda
set _CONDA_ROOT /' | cat - conda/shell/etc/fish/conf.d/conda.fish > conda.fish
  install -Dm 644 conda.fish $pkgdir/etc/fish/conf.d/conda.fish
  echo 'set _CONDA_EXE=/usr/bin/conda
set _CONDA_ROOT=/' | cat - conda/shell/etc/profile.d/conda.csh > conda.csh
  install -Dm 644 conda.csh $pkgdir/etc/profile.d/conda.csh
  echo 'export _CONDA_EXE=/usr/bin/conda
export _CONDA_ROOT=/' | cat - conda/shell/etc/profile.d/conda.sh > conda.sh
  install -Dm 644 conda.sh $pkgdir/etc/profile.d/conda.sh
  install -Dm 644 LICENSE.txt $pkgdir/usr/share/licenses/${pkgname}/LICENSE.txt
}

# vim:set ts=2 sw=2 et:
