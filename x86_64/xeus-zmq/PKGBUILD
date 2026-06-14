# Maintainer: Gregor Kaelin <kaelingre at gmail dot com>

pkgname=xeus-zmq
pkgver=3.1.0
pkgrel=1
pkgdesc="ZeroMQ-based middleware for xeus"
arch=("x86_64")
url="https://github.com/jupyter-xeus/xeus-zmq"
license=('BSD')
depends=('xeus' 'zeromq')
makedepends=('cmake' 'cppzmq')
source=("$pkgname-$pkgver.tar.gz::https://github.com/jupyter-xeus/xeus-zmq/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('55ebfca641e2295dbc0d6c85dbfb54810762bc0792d3e464d32f79a5ce0bdd26')
options=(staticlibs !debug)

build() {
	cd "$pkgname-$pkgver"
	mkdir -p build
	cd build
	cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release ..
	make
}

package() {
	cd "$pkgname-$pkgver/build"
	make DESTDIR="${pkgdir}" install
}
