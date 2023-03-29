# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Ronald van Haren <ronald.archlinux.org>
# Contributor: Damir Perisa <damir.perisa@bluewin.ch>

pkgname=stellarium
pkgver=23.1
pkgrel=2
pkgdesc="Software which renders realistic skies in real time with OpenGL"
arch=(x86_64)
url="https://${pkgname}.org"
license=(GPL2)
depends=('libpng' 'libglvnd' 'freetype2' 'openssl' 'gpsd' 'calcmysky'
  'qt6-charts' 'qt6-serialport' 'qt6-multimedia' 'qt6-positioning' 'qt6-webengine') # 'qxlsx-qt6' 'libindi'
makedepends=('cmake' 'ninja' 'mesa' 'qt6-tools')
source=(https://github.com/Stellarium/${pkgname}/releases/download/v${pkgver}/${pkgname}-${pkgver}.tar.gz{,.asc})
validpgpkeys=('79151C2E6351E7278DA1A730BF38D4D02A328DFF') # Alexander Wolf <alex.v.wolf@gmail.com>
md5sums=('7dde5f42e434fff6aa622cd239385709'
  'SKIP')
sha256sums=('c0d519ef44e78c0609b576c068e1ef2ad09e635d4ff73de7d41bb8c7323bad27'
  'SKIP')

# prepare() {
#   # https://github.com/Stellarium/stellarium/issues/3132#issuecomment-1485304021
#   sed -i 's/SOURCE_SUBDIR QXlsx/SOURCE_SUBDIR QXlsxQt${QT_VERSION_MAJOR}/' ${pkgname}-${pkgver}/CMakeLists.txt
# }

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
    -DPREFER_SYSTEM_INDILIB=No \
    -Wno-dev
  cmake --build build --target all
}

package() {
  DESTDIR="${pkgdir}" cmake --build build --target install
  find "${pkgdir}" -type d -empty -delete
}
