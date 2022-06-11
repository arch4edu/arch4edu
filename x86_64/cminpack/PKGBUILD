pkgname=cminpack
pkgver=1.3.8
pkgrel=3
pkgdesc="A C/C++ rewrite of the MINPACK software"
arch=('x86_64')
url='http://devernay.free.fr/hacks/cminpack/cminpack.html'
license=('BSD')
depends=('cblas')
makedepends=('cmake')
source=("https://github.com/devernay/cminpack/archive/v${pkgver}.tar.gz")
sha256sums=('3ea7257914ad55eabc43a997b323ba0dfee0a9b010d648b6d5b0c96425102d0e')

prepare() {
  cd $srcdir/cminpack-${pkgver}
  # mkl detection
  curl -L https://github.com/devernay/cminpack/pull/51.patch | patch -p1
  curl -L https://github.com/devernay/cminpack/pull/52.patch | patch -p1
}

build() {
  cd $srcdir/cminpack-${pkgver}
  mkdir -p build && pushd build
  cmake -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMINPACK_LIB_INSTALL_DIR=lib \
    -DBUILD_SHARED_LIBS=ON -DBUILD_EXAMPLES=OFF ..
  make
}

package() {
  cd $srcdir/cminpack-${pkgver}/build
  make install DESTDIR="${pkgdir}"
}
