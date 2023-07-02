pkgname=python-time-machine
_pkgname=time_machine
pkgver=2.10.0
pkgrel=2
pkgdesc="Travel through time in your tests."
arch=(any)
url="https://github.com/adamchainz/time-machine"
license=(MIT)
depends=(python-coverage python-pytest-randomly python-dateutil)
makedepends=(python-build python-installer python-wheel python-setuptools)
source=(https://files.pythonhosted.org/packages/source/${_pkgname::1}/$_pkgname/$_pkgname-$pkgver.tar.gz)
sha256sums=('64fd89678cf589fc5554c311417128b2782222dd65f703bf248ef41541761da0')

build() {
  cd ${srcdir}/${_pkgname}-${pkgver}
  python -m build --wheel --no-isolation
}

package() {
  cd ${srcdir}/${_pkgname}-${pkgver}
  python -m installer --destdir="$pkgdir" dist/*.whl
}
