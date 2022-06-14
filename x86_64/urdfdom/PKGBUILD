# Initial Contribution: Benjamin Chretien <chretien at lirmm dot fr>
# Maintainer: Guilhem Saurel <gsaurel at laas dot fr>

pkgname=urdfdom
pkgver=3.1.0
pkgrel=1
pkgdesc="The URDF (U-Robot Description Format) library provides core data structures and a simple XML parsers for populating the class data structures from an URDF file."
arch=('i686' 'x86_64')
url="https://github.com/ros/$pkgname"
license=('BSD')
depends=('tinyxml' 'console-bridge' 'urdfdom-headers')
makedepends=('cmake')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
sha256sums=('fe3bbdfdedbc91359d1be8f094d6a544a941e664ccd6a0c08b061b714e32d216')

build() {
    cmake -B "build-$pkgver" -S "$pkgname-$pkgver" \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_LIBDIR=lib
    cmake --build "build-$pkgver"
}

check() {
    cmake --build "build-$pkgver" -t test
}

package() {
    DESTDIR="$pkgdir/" cmake --install "build-$pkgver"

    # install licence
    install -Dm644 "$pkgname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
