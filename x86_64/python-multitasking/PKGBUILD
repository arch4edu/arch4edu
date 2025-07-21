# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=multitasking
pkgname=python-multitasking
pkgver=0.0.12
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
b2sums=('fbd2708bd8d4303b1614dbf91095e5f2fc937f9f03ca14f855a719947d8e091ac18ef6c59f6978ed86471aa7d41b625ba3bc67007f0ce8c4e7c4e2d8c27e9738')

build() {
    cd $_pkgname-$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
