# Maintainer: Jingbei Li <i@jingbei.li>
# Contributer: Jose Riha <jose1711 gmail com>

pkgname=python-pooch
_pkgname=pooch
pkgver=1.1.1
pkgrel=1
pkgdesc="Python library for fetching and caching data files"
arch=('any')
url="https://www.fatiando.org/pooch/latest/"
license=('BSD 3-Clause')
depends=('python-requests' 'python-packaging' 'python-appdirs')
makedepends=('python-setuptools')
source=("https://github.com/fatiando/pooch/archive/v${pkgver}.tar.gz")
sha512sums=('8593c0b7cd6fdb2d63ec281de6b1e08b03d4dc4959f908b378b10872b68dc7b229ba54f06c514e8b2b195c28c5140fe67c7a5ff9b4620cf82f719baf0b0e83ac')

build() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

