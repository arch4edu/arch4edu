# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Lukas Böger <dev___AT___lboeger___DOT___de>
pkgname=alberta
pkgver=3.0.3
pkgrel=3
pkgdesc="Adaptive multi-Level finite element toolbox"
url="https://www.alberta-fem.de"
license=('GPL2')
arch=('x86_64')
makedepends=('gcc-fortran') # 'blas' 'electricfence' 'duma'
source=("https://gitlab.com/${pkgname}-fem/${pkgname}3/-/archive/releases/${pkgname}3-releases.tar.gz")
sha512sums=('0d502a7123db09d7c54fd8bb59de236a4e76a17d5922adf8b3b6b0e90963a563e4cb6dfda9434bc64fde011fe7f07e9375909fb267b69cb741b457cf645b5d81')

build() {
  cd "${srcdir}/${pkgname}3-releases"
  autoreconf --install
  # for usage within DUNE, add --disable-fem-toolbox to speed up compilation
  ./configure \
    CFLAGS="-I/usr/include/tirpc" \
    LDFLAGS="-ldl -lm -ltirpc" \
    --prefix=/usr \
    --libexecdir=/usr/lib \
    --disable-fem-toolbox \
    --disable-graphics \
    --disable-dependency-tracking \
    --disable-debug \
    --without-gpskca \
    --without-gltools \
    --without-OpenDX \
    --without-grape \
    --without-silo

  make
}

package() {
  cd "${srcdir}/${pkgname}3-releases"

  make install DESTDIR="${pkgdir}"

  install -d ${pkgdir}/usr/share/doc/${pkgname}
  install doc/*.pdf ${pkgdir}/usr/share/doc/${pkgname}
}
