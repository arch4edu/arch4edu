pkgname=cminpack
pkgver=1.3.13
pkgrel=1
pkgdesc="A C/C++ rewrite of the MINPACK software"
arch=('x86_64')
url='http://devernay.free.fr/hacks/cminpack/index.html'
license=('LicenseRef-MINPACK')
depends=('glibc')
makedepends=('cmake')
source=("https://github.com/devernay/cminpack/archive/v${pkgver}.tar.gz")
sha256sums=('cf0d6cc654f8c63bb65979056ea5bcda1046768b1dfe83ceda504924d8331167')

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
