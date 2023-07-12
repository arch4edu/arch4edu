pkgname=python-time-machine
_pkgname=time_machine
pkgver=2.11.0
pkgrel=2
pkgdesc="Travel through time in your tests."
arch=(any)
url="https://github.com/adamchainz/time-machine"
license=(MIT)
depends=(python-coverage python-pytest-randomly python-dateutil)
makedepends=(python-build python-installer python-wheel python-setuptools)
source=(https://files.pythonhosted.org/packages/source/${_pkgname::1}/$_pkgname/$_pkgname-$pkgver.tar.gz)
sha256sums=('6c08a0f9ef8b53ca8b69c0be3f9ddb85a587a784fc239b74c35e6c47bf359515')

build() {
  cd ${srcdir}/${_pkgname}-${pkgver}
  python -m build --wheel --no-isolation
}

package() {
  cd ${srcdir}/${_pkgname}-${pkgver}
  python -m installer --destdir="$pkgdir" dist/*.whl
}
