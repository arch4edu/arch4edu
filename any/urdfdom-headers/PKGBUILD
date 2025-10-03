# Initial Contribution: Benjamin Chretien <chretien at lirmm dot fr>
# Maintainer: Guilhem Saurel <gsaurel at laas dot fr>

_org='ros'
pkgname=urdfdom-headers
_pkgname=urdfdom_headers
pkgver=2.0.0
pkgrel=1
pkgdesc="The URDF (U-Robot Description Format) headers provides core data structure headers for URDF."
arch=('any')
url="https://github.com/$_org/$_pkgname"
license=('BSD-3-Clause')
depends=()
makedepends=('cmake')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
sha256sums=('e12db588ccce52958264f6e4363ca642ab86c328c372e925681a12f7c39d963a')

build() {
    cmake -B "build-$pkgver" -S "$_pkgname-$pkgver" \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -Wno-dev
    cmake --build "build-$pkgver"
}

package() {
    DESTDIR="$pkgdir/" cmake --install "build-$pkgver"

    # install licence
    install -Dm644 "$_pkgname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
