# Initial Contribution: Benjamin Chretien <chretien at lirmm dot fr>
# Maintainer: Guilhem Saurel <gsaurel at laas dot fr>

pkgname=urdfdom-headers
_pkgname=urdfdom_headers
pkgver=1.1.0
pkgrel=1
pkgdesc="The URDF (U-Robot Description Format) headers provides core data structure headers for URDF."
arch=('any')
url="https://github.com/ros/$_pkgname"
license=('BSD')
depends=()
makedepends=('cmake')
source=("$pkgname-$pkgver.tar.gz::https://github.com/ros/$_pkgname/archive/$pkgver.tar.gz")
sha256sums=('01b91c2f7cb42b0033cbdf559684a60001f9927e5d0a5a3682a344cc354f1d39')

build() {
    cmake -B "build-$pkgver" -S "$_pkgname-$pkgver" \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_LIBDIR=lib
    cmake --build "build-$pkgver"
}

package() {
    DESTDIR="$pkgdir/" cmake --install "build-$pkgver"

    # install licence
    install -Dm644 "$_pkgname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
