# Maintainer: Gregor Kaelin <kaelingre at gmail dot com>

pkgname=xeus-zmq
pkgver=4.0.0
pkgrel=1
pkgdesc="ZeroMQ-based middleware for xeus"
arch=("x86_64")
url="https://github.com/jupyter-xeus/xeus-zmq"
license=('BSD')
depends=('xeus>=6' 'zeromq>=4.2.5' 'nlohmann-json>=3.12.0' 'cppzmq>=4.8.1' 'openssl')
makedepends=('cmake' 'cppzmq')
source=("$pkgname-$pkgver.tar.gz::https://github.com/jupyter-xeus/xeus-zmq/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('6a87c0edeefae1350743071cd78c825d6ab21e771b52610ef7e41c434af20db6')
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
