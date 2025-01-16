# Maintainer: Daniel Maslowski <info@orangecms.org>
# Co-Maintainer: Ke Liu <specter119@gmail.com>

pkgname=python-conda-package-handling
pkgver=2.4.0
_srcname="conda-package-handling-${pkgver}"
pkgrel=1
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
  'da690b4ebd76aae8b4de86a443af7d9029c7c5c12c4e0a811f2a9a17481b8f9a1f37f3d7c3bf857171c529ec25b88814342afb023ed75b734c65ac08e33fe067'
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
