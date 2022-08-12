# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Afnan Enayet <afnan at afnan.io>
pkgname=blaze
provides=('blaze')
pkgver=3.8.1
pkgrel=1
pkgdesc='An open-source, high-performance C++ math library for dense and sparse arithmetic.'
url='https://bitbucket.org/blaze-lib/blaze'
arch=('any')
license=('BSD')
makedepends=('cmake' 'git' 'make' 'gcc' 'blas' 'lapack')
sha256sums=('4ad32a786c45285a66a1375b39e65908e604d10596f5863c63b7ef9a13808187')
source=("$pkgname-$pkgver.tar.gz::https://bitbucket.org/blaze-lib/blaze/get/v${pkgver}.tar.gz")
_dir='blaze-lib-blaze-5074d1f16d4b'

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
