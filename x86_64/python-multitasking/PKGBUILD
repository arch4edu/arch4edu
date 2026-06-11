# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=multitasking
pkgname=python-multitasking
pkgver=0.0.13
pkgrel=1
pkgdesc="Non-blocking Python methods using decorators"
arch=(any)
url=https://github.com/ranaroussi/multitasking
license=(Apache-2.0)
depends=(python)
makedepends=(
    python-build
    python-installer
    python-setuptools
    python-wheel
)
source=($_pkgname-$pkgver.tar.gz::https://github.com/ranaroussi/$_pkgname/archive/refs/tags/$pkgver.tar.gz)
b2sums=('3006e6569f312d5154ea3da9bcb4ff8f7d2a3909acc40ac071757f7b889570bb10ae6320406be870ee0e6a7174570fc39a6202bac09ba57ecdec0c0c73226f06')

build() {
    cd $_pkgname-$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
