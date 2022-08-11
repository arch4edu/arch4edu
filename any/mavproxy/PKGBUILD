# Maintainer: Achmad Fathoni <fathoni DOT id AT gmail DOT com>

pkgname=mavproxy
_pkgname=MAVProxy
pkgver=1.8.53
pkgrel=1
pkgdesc='MAVLink proxy and command line ground station.'
arch=('any')
url='https://ardupilot.org/mavproxy'
license=('GPL3')
depends=(python python-pymavlink python-opencv)
makedepends=(python python-setuptools)
source=("https://files.pythonhosted.org/packages/source/${_pkgname::1}/$_pkgname/$_pkgname-$pkgver.tar.gz")
sha256sums=('e9ac4218c32ebe7e1e71be38b40073fe66e5c39bb58d2c31d622fac6ff03c8a3')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir" --optimize=1
}
