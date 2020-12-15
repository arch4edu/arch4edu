# Initial Contribution: Benjamin Chretien <chretien at lirmm dot fr>
# Maintainer: Guilhem Saurel <gsaurel at laas dot fr>

pkgname=urdfdom
pkgver=1.0.4
pkgrel=4
pkgdesc="The URDF (U-Robot Description Format) library provides core data structures and a simple XML parsers for populating the class data structures from an URDF file."
arch=('i686' 'x86_64')
url="https://github.com/ros/$pkgname"
license=('BSD')
depends=('tinyxml' 'console-bridge' 'urdfdom-headers')
makedepends=('cmake')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz"
    $url/pull/141.patch)
sha256sums=('8f3d56b0cbc4b84436d8baf4c8346cd2ee7ffb257bba5ddd9892c41bf516edc4'
    'fc50cc69d0be8eab567b73f13376769b026255baac2d97d50a5f10ca5a6189e5')

prepare() {
    cd "$pkgbase-$pkgver"

    # ref https://github.com/ros/urdfdom/pull/141
    patch -p1 -i "$srcdir/141.patch"
}

build() {
    cd "$pkgname-$pkgver"
    cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=lib .
    make
}

package() {
    cd "$pkgname-$pkgver"
    make DESTDIR="$pkgdir/" install
    install -D -m644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
