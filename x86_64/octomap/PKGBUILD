# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Andrew Sun <adsun701 at gmail dot com>
# Contributor: Benjamin Chrétien <chretien dot b+arch at gmail dot com>
# Contributor: Soo-Hyun Yoo <yoos117 at gmail dot com>

pkgname=octomap
pkgver=1.9.8
pkgrel=1
pkgdesc="Efficient probabilistic 3D mapping framework based on octrees"
arch=('i686' 'x86_64')
url="https://octomap.github.io/"
license=('BSD')
depends=('gcc-libs')
makedepends=('cmake')
provides=('octomap')
conflicts=('octomap-git')
options=('staticlibs')
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/OctoMap/octomap/archive/v${pkgver}.tar.gz"
        "iterator.patch::https://patch-diff.githubusercontent.com/raw/OctoMap/octomap/pull/373.patch")
sha256sums=('417af6da4e855e9a83b93458aa98b01a2c88f880088baad2b59d323ce162586e'
            'SKIP')

prepare() {
    cd "$srcdir/octomap-$pkgver"
    patch -Np1 -i "$srcdir/iterator.patch"
}

build() {
    cd "$srcdir/octomap-$pkgver/octomap"
    mkdir build && cd build
    cmake .. \
        -DCMAKE_INSTALL_PREFIX=/usr
    make
}

package() {
    cd "$srcdir/octomap-$pkgver/octomap"
    cd build
    make DESTDIR="${pkgdir}" install
    install -Dm644 ../LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}
