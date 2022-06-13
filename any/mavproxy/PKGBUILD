# Maintainer: Achmad Fathoni <fathoni DOT id AT gmail DOT com>

pkgname=mavproxy
_pkgname=MAVProxy
pkgver=1.8.50
pkgrel=1
pkgdesc='MAVLink proxy and command line ground station.'
arch=('any')
url='https://ardupilot.org/mavproxy'
license=('GPL3')
depends=(python python-pymavlink python-opencv)
makedepends=(python python-setuptools)
source=("https://files.pythonhosted.org/packages/source/${_pkgname::1}/$_pkgname/$_pkgname-$pkgver.tar.gz")
sha256sums=('7537579a19bab1666984b85ca0a44343622bd2172ed1ebf4c42ba5d8ef610178')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir" --optimize=1
}
