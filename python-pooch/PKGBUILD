# Maintainer: Jingbei Li <i@jingbei.li>
# Contributer: Jose Riha <jose1711 gmail com>

pkgname=python-pooch
_pkgname=pooch
pkgver=1.3.0
pkgrel=1
pkgdesc="Python library for fetching and caching data files"
arch=('any')
url="https://www.fatiando.org/pooch/latest/"
license=('BSD 3-Clause')
depends=('python-requests' 'python-packaging' 'python-appdirs')
makedepends=('python-setuptools')
source=("https://github.com/fatiando/pooch/archive/v${pkgver}.tar.gz")
sha512sums=('29f64cade776e76e1bed66dc854be70c0a2abaca0fc8ae39ffe25ba9c6f81bb8c9fcf36ad89c005268111fe7702814126a0ba882e7660d8b6e8b4535877c9a67')

build() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}


