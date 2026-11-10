# Initial Contribution: Benjamin Chretien <chretien at lirmm dot fr>
# Maintainer: Guilhem Saurel <gsaurel at laas dot fr>

_org='ros'
pkgname=urdfdom-headers
_pkgname=urdfdom_headers
pkgver=3.0.1
pkgrel=1
pkgdesc="The URDF (U-Robot Description Format) headers provides core data structure headers for URDF."
arch=('any')
url="https://github.com/$_org/$_pkgname"
license=('BSD-3-Clause')
depends=()
makedepends=('cmake')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
sha256sums=('42d85a82d1dea2e1252596131e58997244ce6c59d12ae9ab852fe7c35d09f0ec')

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
