# Maintainer: Sylvain POULAIN <sylvain dot poulain at giscan dot com>

pkgname=lerc
pkgver=4.1.1
pkgrel=1
pkgdesc='Limited Error Raster Compression library'
arch=('x86_64')
url='https://github.com/Esri/lerc'
license=('Apache-2.0')
makedepends=('cmake')
source=("https://github.com/Esri/lerc/archive/refs/tags/v$pkgver.tar.gz")
b2sums=('37e8833c5facf54ee73011e983ecd3fae9ea0d12756e19a06900306225960b71b229efd98a139ba9480ace7e684865ba40faa1aa2ffa6f0aba6b697bc7459fcc')

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
