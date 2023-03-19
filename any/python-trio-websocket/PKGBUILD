# Maintainer: Achmad Fathoni<fathoni.id(at)gmail.com>
# Maintainer: Michał Wojdyła < micwoj9292 at gmail dot com >
pkgname=python-trio-websocket
_pkgname=${pkgname:7}
pkgver=0.10.1
pkgrel=1
pkgdesc="WebSocket library for Trio"
arch=('any')
url="https://pypi.org/project/${_pkgname}"
license=(MIT)
makedepends=(python-build python-installer python-wheel python-setuptools)
depends=(python python-exceptiongroup python-trio python-wsproto)
source=(https://files.pythonhosted.org/packages/source/${_pkgname::1}/$_pkgname/$_pkgname-$pkgver.tar.gz)
sha256sums=('e469c0182e36cbd5cbab4f555ea584c3d1e7c67f9dfe990efad0dffbeac292ac')

build() {
    cd ${srcdir}/${_pkgname}-${pkgver}
    python -m build --wheel --no-isolation
}

package() {
    cd ${srcdir}/${_pkgname}-${pkgver}
    python -m installer --destdir="$pkgdir" dist/*.whl
}
