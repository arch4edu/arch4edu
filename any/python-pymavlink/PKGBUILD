# Maintainer: acxz <akashpatel2008 at yahoo dot com>

pkgname=python-pymavlink
pkgver=2.4.41
pkgrel=1
pkgdesc='python MAVLink interface and utilities'
arch=('any')
url='https://github.com/ArduPilot/pymavlink/'
license=('LGPL v3')
depends=(python python-future python-lxml)
makedepends=(python python-build python-installer python-wheel python-setuptools)
source=("$pkgname-$pkgver.tar.gz::https://pypi.org/packages/source/p/pymavlink/pymavlink-${pkgver}.tar.gz")
sha256sums=('ed3225ce985d06103aab251afc883d04a98a1d6db5c73995e7de4caacb1f66cd')

_pkgname=pymavlink

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
