pkgname=cminpack
pkgver=1.3.9
pkgrel=1
pkgdesc="A C/C++ rewrite of the MINPACK software"
arch=('x86_64')
url='http://devernay.free.fr/hacks/cminpack/cminpack.html'
license=('BSD')
depends=('cblas')
makedepends=('cmake')
source=("https://github.com/devernay/cminpack/archive/v${pkgver}.tar.gz")
sha256sums=('aa37bac5b5caaa4f5805ea5c4240e3834c993672f6dab0b17190ee645e251c9f')

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
