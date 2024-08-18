# Maintainer: Daniel Maslowski <info@orangecms.org>
# Co-Maintainer: Ke Liu <specter119@gmail.com>

pkgname=python-conda-package-handling
pkgver=2.3.0
_srcname="conda-package-handling-${pkgver}"
pkgrel=3
pkgdesc="Create and extract conda package of various formats"
arch=('any')
url="https://github.com/conda/conda-package-handling"
license=('BSD-3-Clause')
depends=(
  python
  python-conda-package-streaming
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  cython
)
options=(!emptydirs)
install=
source=(
  "${_srcname}.tar.gz::$url/archive/$pkgver.tar.gz"
)
sha512sums=(
  'f4e16c1e8a33fe92c70fd48e42d77247fd705eaea1ee8a9e95c52bdcf942a5334bb0b4f3f6492fd0e5defd3f724854b353999350b30bc507d77cc611af6f4c41'
)

build() {
  cd "$srcdir/${_srcname}"
  sed -i 's/archive_and_deps/archive/' setup.py
  python setup.py clean --all
  python setup.py build
}

package() {
  cd "$srcdir/${_srcname}"
  python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
  install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
