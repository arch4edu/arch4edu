# Maintainer: Sylvain POULAIN <sylvain dot poulain at giscan dot com>

pkgname=lerc
pkgver=4.0.0
pkgrel=2
pkgdesc='Limited Error Raster Compression library'
arch=('x86_64')
url='https://github.com/Esri/lerc'
license=('Apache-2.0')
makedepends=('cmake')
source=("https://github.com/Esri/lerc/archive/refs/tags/v$pkgver.tar.gz")
b2sums=('b4c593ab2d28ad4c03149267db7d181462bc2977f6c908c88e7f769fed720be900936550e27cecfe32ee16b410c8a7885c1e509ae26717b5719e602922de305a')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  [[ -d build ]] || mkdir build

  cd "${srcdir}/${pkgname}-${pkgver}/build"

  cmake -G "Unix Makefiles" .. \
  -DCMAKE_BUILD_TYPE="Release" \
  -DCMAKE_INSTALL_PREFIX:PATH=/usr/
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}/build"

  make DESTDIR="${pkgdir}" install

}
