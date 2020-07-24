# Initial Contribution: Benjamin Chretien <chretien at lirmm dot fr>
# Maintainer: Guilhem Saurel <gsaurel at laas dot fr>

pkgname=console-bridge
_pkgname=console_bridge
pkgver=1.0.1
pkgrel=1
pkgdesc="A ROS-independent package for logging that seamlessly pipes into rosconsole/rosout for ROS-dependent packages."
arch=('i686' 'x86_64')
url="http://www.ros.org/"
license=('BSD')
depends=('gcc-libs')
makedepends=('cmake')
source=("https://github.com/ros/$_pkgname/archive/$pkgver.tar.gz")
sha256sums=('2ff175a9bb2b1849f12a6bf972ce7e4313d543a2bbc83b60fdae7db6e0ba353f')

build() {
    cd "$_pkgname-$pkgver"
    cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=lib .
    make
}

package() {
    cd "$_pkgname-$pkgver"
    make DESTDIR="$pkgdir/" install
    install -D -m644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
