# Contributor: Graziano Giuliani
# Maintainer : Austin Cross <austincross@gmail.com>
pkgname=g2clib
pkgver=1.9.0
pkgrel=1
pkgdesc="GRIB2 encoder/decoder (C version)"
url="https://github.com/NOAA-EMC/NCEPLIBS-g2c"
license=('LGPL-3.0-only')
arch=('i686' 'x86_64')
provides=(g2clib)
depends=(cmake jasper libpng)
options=('staticlibs')
source=("$pkgname-$pkgver.tar.gz::https://github.com/NOAA-EMC/NCEPLIBS-g2c/archive/refs/tags/v${pkgver}.tar.gz")
md5sums=('2e5c82a6ff9c619db682d7115a57db62')

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
