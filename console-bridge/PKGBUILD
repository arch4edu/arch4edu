# Initial Contribution: Benjamin Chretien <chretien at lirmm dot fr>
# Maintainer: Guilhem Saurel <gsaurel at laas dot fr>

pkgname=console-bridge
_pkgname=console_bridge
pkgver=1.0.0
pkgrel=2
pkgdesc="A ROS-independent package for logging that seamlessly pipes into rosconsole/rosout for ROS-dependent packages."
arch=('i686' 'x86_64')
url="http://www.ros.org/"
license=('BSD')
depends=('gcc-libs')
makedepends=('cmake')
source=("https://github.com/ros/$_pkgname/archive/$pkgver.tar.gz")
sha256sums=('880bbded7fcdc71479e9b1efc3ba5353f08eed23f0009c93d6bea8ba3974d078')

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
