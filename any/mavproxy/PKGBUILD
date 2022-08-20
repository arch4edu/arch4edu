# Maintainer: Achmad Fathoni <fathoni DOT id AT gmail DOT com>

pkgname=mavproxy
_pkgname=MAVProxy
pkgver=1.8.54
pkgrel=1
pkgdesc='MAVLink proxy and command line ground station.'
arch=('any')
url='https://ardupilot.org/mavproxy'
license=('GPL3')
depends=(python python-pymavlink python-opencv)
makedepends=(python python-setuptools)
source=("https://files.pythonhosted.org/packages/source/${_pkgname::1}/$_pkgname/$_pkgname-$pkgver.tar.gz")
sha256sums=('5df1a342f0407a8effb07da11583b553ba8de35d43d35a26fd0fe38c7c753bc6')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir" --optimize=1
}
