# Contributor: insmtr <insmtr@insmtr.cn>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=python-pymavlink
pkgver=2.4.49
pkgrel=1
pkgdesc='python MAVLink interface and utilities'
arch=('any')
url='https://github.com/ArduPilot/pymavlink/'
license=('LGPL v3')
depends=(python python-lxml cython)
makedepends=(python python-build python-installer python-wheel python-setuptools)
source=("$pkgname-$pkgver.tar.gz::https://pypi.org/packages/source/p/pymavlink/pymavlink-${pkgver}.tar.gz")
sha256sums=('d7cf10d5592d038a18aa972711177ebb88be2143efcc258df630b0513e9da2c2')

_pkgname=pymavlink

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
