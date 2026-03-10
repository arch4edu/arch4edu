# Maintainer: Sylvain POULAIN <sylvain dot poulain at giscan dot com>

pkgname=lerc
pkgver=4.1.0
pkgrel=1
pkgdesc='Limited Error Raster Compression library'
arch=('x86_64')
url='https://github.com/Esri/lerc'
license=('Apache-2.0')
makedepends=('cmake')
source=("https://github.com/Esri/lerc/archive/refs/tags/v$pkgver.tar.gz")
b2sums=('48613979299445ae82b2ac57f45a116eb699acab78c5c17c93201885f92fb49124e785a187c82df5df66e5e27103c67be4606c98b1d6089fc5d1418075604e44')

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
