# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Cong Gu <gucong43216@gmail.com>
pkgname=zoltan
pkgver=3.901
pkgrel=1
pkgdesc="Parallel Partitioning, Load Balancing and Data-Management Services"
arch=('x86_64')
url="https://github.com/sandialabs/${pkgname}"
license=(LGPL)
depends=(scotch parmetis)
conflicts=('trilinos')
source=(${url}/archive/v${pkgver}.tar.gz)
sha512sums=('e7c1e65abb0592cd16c0a8c5d4b98dc14001ed0a3169a66ed5cc28dbe621fefd9da7d05a584337d546301201a4b128233e659baa7c5c00ba5b92109cb0217306')

prepare() {
  [ -d build ] && rm -r build
  mkdir -p build
}

build() {
  cd build

  ../Zoltan-${pkgver}/configure \
    --prefix=/usr \
    --enable-mpi --with-mpi-compilers \
    --with-mpi-incdir="/usr/include" \
    --with-mpi-libdir="/usr/lib/openmpi" \
    --with-gnumake \
    --with-scotch \
    --with-scotch-incdir="/usr/include/scotch" \
    --with-scotch-libdir="/usr/lib" \
    --with-parmetis \
    --with-parmetis-incdir="/usr/include" \
    --with-parmetis-libdir="/usr/lib" \
    --with-ar='$(CXX) -shared $(LDFLAGS) -o' \
    --with-cflags="-fPIC" \
    --with-cxxflags="-fPIC" \
    --with-ldflags="-L/usr/lib/openmpi -lptscotch  -lptscotcherr -lptscotcherrexit -lscotch -lscotcherr -lscotcherrexit -lparmetis -lmetis -lmpi  -lm" \
    RANLIB=echo

  make
}

package() {
  cd "${srcdir}/build"

  make DESTDIR="${pkgdir}/" install
  install -Dm777 "${pkgdir}/usr/lib/libzoltan.a" "${pkgdir}/usr/lib/libzoltan.so"

  install -Dm644 ${srcdir}/Zoltan-${pkgver}/COPYRIGHT_AND_LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
