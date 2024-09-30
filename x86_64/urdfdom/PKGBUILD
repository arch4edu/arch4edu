# Initial Contribution: Benjamin Chretien <chretien at lirmm dot fr>
# Maintainer: Guilhem Saurel <gsaurel at laas dot fr>

_org='ros'
_pkgname=urdfdom
pkgname="$_pkgname"
pkgver=4.0.1
pkgrel=1
pkgdesc="The URDF (U-Robot Description Format) library provides core data structures and a simple XML parsers for populating the class data structures from an URDF file."
arch=('i686' 'x86_64')
url="https://github.com/$_org/$_pkgname"
license=('BSD-3-Clause')
depends=('tinyxml2' 'console-bridge' 'urdfdom-headers' 'gcc-libs' 'glibc')
makedepends=('cmake')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
sha256sums=('46b122c922f44ec32674a56e16fd4b5d068b53265898cbea2c3e1939ecccc62a')

build() {
    cmake -B "build-$pkgver" -S "$pkgbase-$pkgver" \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -Wno-dev
    cmake --build "build-$pkgver"
}

check() {
    cmake --build "build-$pkgver" -t test
}

package() {
    DESTDIR="$pkgdir/" cmake --build "build-$pkgver" -t install
    install -Dm644 "$pkgbase-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
