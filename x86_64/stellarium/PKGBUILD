# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Ronald van Haren <ronald.archlinux.org>
# Contributor: Damir Perisa <damir.perisa@bluewin.ch>

pkgname=stellarium
pkgver=1.2
pkgrel=1
pkgdesc="Software which renders realistic skies in real time with OpenGL"
arch=(x86_64)
url="https://${pkgname}.org"
license=(GPL2)
depends=('libpng' 'libglvnd' 'freetype2' 'openssl' 'gpsd' 'calcmysky' 'libindi'
  'qt6-charts' 'qt6-serialport' 'qt6-multimedia' 'qt6-positioning' 'qt6-webengine') # 'qxlsx'
makedepends=('cmake' 'ninja' 'mesa' 'qt6-tools')
source=(https://github.com/Stellarium/${pkgname}/releases/download/v${pkgver}/${pkgname}-${pkgver}.tar.gz{,.asc})
validpgpkeys=('79151C2E6351E7278DA1A730BF38D4D02A328DFF') # Alexander Wolf <alex.v.wolf@gmail.com>
md5sums=('1a9b2b69300ac54fda47cf4b801bf07f'
         'SKIP')
sha256sums=('2cbf95839c5fbd312c08ad0f92b2ddf8a7f822bd32bc31e91f3aa28920674f60'
            'SKIP')

build() {
  PATH="/usr/bin/core_perl/:$PATH"
  cmake \
    -S ${pkgname}-${pkgver} \
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
