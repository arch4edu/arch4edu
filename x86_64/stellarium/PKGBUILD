# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Ronald van Haren <ronald.archlinux.org>
# Contributor: Damir Perisa <damir.perisa@bluewin.ch>

pkgname=stellarium
pkgver=23.4
pkgrel=4
pkgdesc="Software which renders realistic skies in real time with OpenGL"
arch=(x86_64)
url="https://${pkgname}.org"
license=(GPL2)
depends=(nlopt libpng libglvnd freetype2 openssl gpsd calcmysky qt6-charts qt6-serialport
  qt6-multimedia qt6-positioning qt6-webengine qxlsx-qt6) # libindi
makedepends=(cmake ninja mesa qt6-tools)                  # doxygen graphviz
optdepends=('man-db: manual pages for stellarium')
source=(https://github.com/Stellarium/${pkgname}/releases/download/v${pkgver}/${pkgname}-${pkgver}.tar.gz{,.asc})
validpgpkeys=('79151C2E6351E7278DA1A730BF38D4D02A328DFF') # Alexander Wolf <alex.v.wolf@gmail.com>
md5sums=('6107d1e352216b1e20d3cf3d45cea277'
  'SKIP')
sha256sums=('db4db9f205cc13fb68e3f3c4c895754d16868e4d25a14da44db6d0d809e39943'
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
    -DCMAKE_C_EXTENSIONS=Yes \
    -DCMAKE_CXX_COMPILER=g++ \
    -DCMAKE_C_STANDARD=17 \
    -DCMAKE_CXX_EXTENSIONS=Yes \
    -DENABLE_QT6=1 \
    -DENABLE_SHOWMYSKY=ON \
    -DENABLE_TESTING=0 \
    -DENABLE_XLSX=1 \
    -DPREFER_SYSTEM_INDILIB=No \
    -Wno-dev
  cmake --build build --target all
}

package() {
  DESTDIR="${pkgdir}" cmake --build build --target install
  install -Dm 644 ${pkgname}-${pkgver}/COPYING -t "${pkgdir}/usr/share/licenses/${pkgname}"
  find "${pkgdir}" -type d -empty -delete
}
