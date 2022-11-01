# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Ronald van Haren <ronald.archlinux.org>
# Contributor: Damir Perisa <damir.perisa@bluewin.ch>

pkgname=stellarium
pkgver=1.1.1
pkgrel=2
pkgdesc="Software which renders realistic skies in real time with OpenGL"
arch=(x86_64)
url="https://${pkgname}.org"
license=(GPL2)
depends=('libpng' 'libglvnd' 'freetype2' 'openssl' 'gpsd' 'calcmysky' 'libindi'
  'qt6-charts' 'qt6-serialport' 'qt6-multimedia' 'qt6-positioning' 'qt6-webengine') # 'qxlsx'
makedepends=('cmake' 'ninja' 'mesa' 'qt6-tools')
source=(https://github.com/Stellarium/${pkgname}/releases/download/v${pkgver::-2}/${pkgname}-${pkgver}.tar.gz{,.asc})
validpgpkeys=('79151C2E6351E7278DA1A730BF38D4D02A328DFF') # Alexander Wolf <alex.v.wolf@gmail.com>
md5sums=('0f9247e48dd311ec9663a0e0d3b925ef'
  'SKIP')
sha256sums=('d2844eae0b62761a04fe04324f65f43d852c590d3249f287e181701822e3766e'
  'SKIP')

build() {
  PATH="/usr/bin/core_perl/:$PATH"
  cmake \
    -S ${pkgname}-${pkgver::-2} \
    -B build \
    -G Ninja \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_C_COMPILER=gcc \
    -DCMAKE_CXX_STANDARD=17 \
    -DCMAKE_C_EXTENSIONS=No \
    -DCMAKE_CXX_COMPILER=g++ \
    -DCMAKE_C_STANDARD=11 \
    -DCMAKE_CXX_EXTENSIONS=No \
    -DENABLE_QT6=1 \
    -DENABLE_SHOWMYSKY=ON \
    -DENABLE_TESTING=0 \
    -DENABLE_XLSX=0 \
    -Wno-dev
  cmake --build build --target all
}

package() {
  DESTDIR="${pkgdir}" cmake --build build --target install
  find "${pkgdir}" -type d -empty -delete
}
