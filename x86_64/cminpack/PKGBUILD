pkgname=cminpack
pkgver=1.3.10
pkgrel=1
pkgdesc="A C/C++ rewrite of the MINPACK software"
arch=('x86_64')
url='http://devernay.free.fr/hacks/cminpack/cminpack.html'
license=('BSD')
depends=('cblas')
makedepends=('cmake')
source=("https://github.com/devernay/cminpack/archive/v${pkgver}.tar.gz")
sha256sums=('6355776f60ebfeef63883aa02c19ab57f1ba776e43122f27cb3161e7fc277d1d')

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
