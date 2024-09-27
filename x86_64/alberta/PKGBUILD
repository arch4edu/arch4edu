# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Lukas Böger <dev___AT___lboeger___DOT___de>
pkgname=alberta
pkgver=3.1.0
pkgrel=3
pkgdesc="Adaptive multi-Level finite element toolbox"
url="https://www.${pkgname}-fem.de"
license=(GPL2)
arch=(x86_64)
makedepends=(gcc-fortran) # blas electricfence duma
source=(https://gitlab.com/${pkgname}-fem/${pkgname}3/-/archive/v${pkgver}/${pkgname}3-v${pkgver}.tar.gz)
sha512sums=('1f206d4123db6792e0dbd8394cb01aa963678fceb28d2f0efbba99c887fc2043b1706529d05386e156abf7d19fe0c26f8c2be642e4ea0ab63eef5d2f68e3cfd0')

prepare() {
  sed -i 's/dist_gnucompat_DATA/#dist_gnucompat_DATA/' ${pkgname}3-v${pkgver}/gnu-compat/Makefile.am
}

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
    --quiet \
    CC="gcc -Wno-error=incompatible-pointer-types -B/usr/bin/mold"
  # https://github.com/xmlsec/python-xmlsec/issues/323#issuecomment-2137419853
  # ../../../../alberta/tests/graphics.c:163:26: error: passing argument 2 of ‘graph_drv_d’ from incompatible pointer type [-Wincompatible-pointer-types]
  # 163 |     graph_drv_d(win_val, u_h, 0.0, 0.0, refine);
  make V=0
}

check() {
  cd ${pkgname}3-v${pkgver}
  make check V=0
}

package() {
  cd ${pkgname}3-v${pkgver}
  make install DESTDIR="${pkgdir}"
  install -Dm644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}"
}
