pkgname=cminpack
pkgver=1.3.11
pkgrel=1
pkgdesc="A C/C++ rewrite of the MINPACK software"
arch=('x86_64')
url='http://devernay.free.fr/hacks/cminpack/index.html'
license=('BSD')
depends=('cblas')
makedepends=('cmake')
source=("https://github.com/devernay/cminpack/archive/v${pkgver}.tar.gz")
sha256sums=('45675fac0a721a1c7600a91a9842fe1ab313069db163538f2923eaeddb0f46de')

build() {
  cd $srcdir/cminpack-${pkgver}
  cmake -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=ON -DBUILD_EXAMPLES=OFF -B build .
  make -C build
}

package() {
  cd $srcdir/cminpack-${pkgver}/build
  make install DESTDIR="${pkgdir}"
}
