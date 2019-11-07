# Initial Contribution: Benjamin Chretien <chretien at lirmm dot fr>
# Maintainer: Guilhem Saurel <gsaurel at laas dot fr>

pkgname=console-bridge
_pkgname=console_bridge
pkgver=0.4.1
pkgrel=1
pkgdesc="A ROS-independent package for logging that seamlessly pipes into rosconsole/rosout for ROS-dependent packages."
arch=('i686' 'x86_64')
url="http://www.ros.org/"
license=('BSD')
depends=('gcc-libs')
makedepends=('cmake')
source=("https://github.com/ros/$_pkgname/archive/$pkgver.tar.gz")
md5sums=('6bb0f640db1712cf2277e7923e7bab68')

build() {
    cd "$_pkgname-$pkgver"
    cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=lib .
    make
}

package() {
    cd "$_pkgname-$pkgver"
    make DESTDIR="$pkgdir/" install
    mkdir -p $pkgdir/usr/share/licenses/$pkgname
    head -n 33 $pkgdir/usr/include/console_bridge/console.h > $pkgdir/usr/share/licenses/$pkgname/LICENSE
}
