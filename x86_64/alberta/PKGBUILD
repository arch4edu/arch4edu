# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Lukas Böger <dev___AT___lboeger___DOT___de>
pkgname=alberta
pkgver=3.1.1
pkgrel=2
pkgdesc="Adaptive multi-Level finite element toolbox"
url="https://www.${pkgname}-fem.de"
license=(GPL-2.0-or-later)
arch=(x86_64)
makedepends=(gcc-fortran texlive-latexextra texlive-plaingeneric texlive-fontutils) # blas electricfence duma
source=(https://gitlab.com/${pkgname}-fem/${pkgname}3/-/archive/v${pkgver}/${pkgname}3-v${pkgver}.tar.gz)
sha512sums=('c3912500cf9181be075a5a79f75646cf69539f268e151ff0a33cd1099f379dc2d8b868bd9772d91c43ae9457cb7e658d3cd7b72534b81ccee802a9aac163c3f0')

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
    CC="gcc -B/usr/bin/mold"
  make V=0
  make doc/alberta-book
  make doc/alberta-man
}

check() {
  cd ${pkgname}3-v${pkgver}
  make check V=0
}

package() {
  cd ${pkgname}3-v${pkgver}
  make install DESTDIR="${pkgdir}"
  install -d ${pkgdir}/usr/share/doc/${pkgname}
  install doc/*.pdf ${pkgdir}/usr/share/doc/${pkgname}
  install -Dm644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}"
}
