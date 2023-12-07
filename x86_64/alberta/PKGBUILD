# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Lukas Böger <dev___AT___lboeger___DOT___de>
pkgname=alberta
pkgver=3.1.0
pkgrel=1
pkgdesc="Adaptive multi-Level finite element toolbox"
url="https://www.alberta-fem.de"
license=(GPL2)
arch=(x86_64)
makedepends=(gcc-fortran) # blas electricfence duma
source=(https://gitlab.com/${pkgname}-fem/${pkgname}3/-/archive/v${pkgver}/${pkgname}3-v${pkgver}.tar.gz)
sha512sums=('1f206d4123db6792e0dbd8394cb01aa963678fceb28d2f0efbba99c887fc2043b1706529d05386e156abf7d19fe0c26f8c2be642e4ea0ab63eef5d2f68e3cfd0')

build() {
  cd ${pkgname}3-v${pkgver}
  ./generate-alberta-automakefiles.sh
  autoreconf --force --install
  # for usage within DUNE, add --disable-fem-toolbox to speed up compilation
  ./configure \
    --prefix=/usr \
    --libexecdir=/usr/lib \
    --enable-dim-of-world="4 5" \
    --disable-debug \
    --disable-graphics \
    --disable-waiting-in-tests \
    --without-gpskca \
    --without-gltools \
    --without-OpenDX \
    --without-grape \
    --without-silo \
    CC="gcc -B/usr/bin/mold"

  make
}

check() {
  cd ${pkgname}3-v${pkgver}
  make distcheck
}

package() {
  cd ${pkgname}3-v${pkgver}
  make install DESTDIR="${pkgdir}"
  install -Dm644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}"
}
