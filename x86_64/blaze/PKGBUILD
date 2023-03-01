# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Afnan Enayet <afnan at afnan.io>
pkgname=blaze
provides=('blaze')
pkgver=3.8.2
pkgrel=1
pkgdesc='An open-source, high-performance C++ math library for dense and sparse arithmetic.'
url='https://bitbucket.org/blaze-lib/blaze'
arch=('any')
license=('BSD')
makedepends=('cmake' 'git' 'make' 'gcc' 'blas' 'lapack')
sha256sums=('13a2199e75b7a8540e84032b0b4aaff93148a8d221e2d410230d7a58f5dfbbd5')
source=("$pkgname-$pkgver.tar.gz::https://bitbucket.org/blaze-lib/blaze/get/v${pkgver}.tar.gz")
_dir='blaze-lib-blaze-3156507a4b7a'

build() {
    cd $_dir
    mkdir -p build
    cd build
    cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release ..
    make
}

package() {
    cd $_dir/build
    make DESTDIR="$pkgdir/" install
}
