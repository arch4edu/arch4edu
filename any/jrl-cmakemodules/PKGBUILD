# Maintainer: Guilhem Saurel <saurel@laas.fr>

_org='jrl-umi3218'
_pkgname=jrl-cmakemodules
pkgname=$_pkgname
pkgver=2.4.0
pkgrel=1
pkgdesc="CMake utility toolbox"
arch=('any')
url="https://github.com/$_org/$_pkgname"
license=('LGPL-3.0-or-later')
makedepends=('cmake' 'python' 'python-numpy' 'perl' 'bash')
source=("${_pkgname}-${pkgver}.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('1e810d43d471e9a172458187fd5ec0746d3155e173f4fb387e6c7fb56906d359')

build() {
    cmake -B "build-$pkgver" -S "$pkgbase-$pkgver" \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -Wno-dev
    cmake --build "build-$pkgver"
}

package() {
    DESTDIR="$pkgdir/" cmake --build "build-$pkgver" -t install
    install -Dm644 "$pkgbase-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
