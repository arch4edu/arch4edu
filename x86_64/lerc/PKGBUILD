# Maintainer: Sylvain POULAIN <sylvain dot poulain at giscan dot com>

pkgname=lerc
pkgver=3.0
pkgrel=1
pkgdesc='Limited Error Raster Compression library'
arch=('x86_64')
url='https://github.com/Esri/lerc'
license=('Apache-2.0')
depends=('python' 'python-numpy')
makedepends=('cmake')
source=("https://github.com/Esri/lerc/archive/refs/tags/v$pkgver.tar.gz")
sha512sums=('8e04d890c4d46528641b354ec3f47f2b0563e1740927ac894925a30f7de2b235cb3517ce7e477886bd3eb50ebd6c6e78f22d73d5500877e552d9e684e626293b')

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
