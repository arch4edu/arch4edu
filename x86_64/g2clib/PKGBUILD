# Contributor: Graziano Giuliani
# Maintainer : Austin Cross <austincross@gmail.com>
pkgname=g2clib
pkgver=2.1.0
pkgrel=1
pkgdesc="GRIB2 encoder/decoder (C version)"
url="https://github.com/NOAA-EMC/NCEPLIBS-g2c"
license=('LGPL-3.0-only')
arch=('i686' 'x86_64')
provides=(g2clib)
depends=(cmake jasper libpng)
options=('staticlibs')
source=("$pkgname-$pkgver.tar.gz::https://github.com/NOAA-EMC/NCEPLIBS-g2c/archive/refs/tags/v${pkgver}.tar.gz")
md5sums=('bf11e8ff0472afd8eb04188368d9911b')

build() {
  cmake -B build -S "NCEPLIBS-g2c-${pkgver}" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/usr' \
        -Wno-dev
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}

# vim:set ts=2 sw=2 et:
