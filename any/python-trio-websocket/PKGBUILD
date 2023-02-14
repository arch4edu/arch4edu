# Maintainer: Achmad Fathoni<fathoni.id(at)gmail.com>
pkgname=python-trio-websocket
_pkgname=${pkgname:7}
pkgver=0.9.2
pkgrel=3
pkgdesc="WebSocket library for Trio"
arch=('any')
url="https://pypi.org/project/${_pkgname}"
license=(MIT)
makedepends=(python-build python-installer python-wheel python-setuptools)
depends=(python python-async_generator python-trio python-wsproto)
source=(https://files.pythonhosted.org/packages/source/${_pkgname::1}/$_pkgname/$_pkgname-$pkgver.tar.gz)
sha256sums=('a3d34de8fac26023eee701ed1e7bf4da9a8326b61a62934ec9e53b64970fd8fe')

build() {
    cd ${srcdir}/${_pkgname}-${pkgver}
    python -m build --wheel --no-isolation
}

package() {
    cd ${srcdir}/${_pkgname}-${pkgver}
    python -m installer --destdir="$pkgdir" dist/*.whl
}
