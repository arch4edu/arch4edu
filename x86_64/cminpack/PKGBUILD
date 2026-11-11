pkgname=cminpack
pkgver=1.3.15
pkgrel=1
pkgdesc="A C/C++ rewrite of the MINPACK software"
arch=('x86_64')
url='http://devernay.free.fr/hacks/cminpack/index.html'
license=('LicenseRef-MINPACK')
depends=('glibc')
makedepends=('cmake')
source=("https://github.com/devernay/cminpack/archive/v${pkgver}.tar.gz")
sha256sums=('4bcc2fb514809eaa7bfecf2f2f663f3f0988a425ff64615316f5c4ed68757b97')

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
