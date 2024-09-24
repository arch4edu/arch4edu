# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Ronald van Haren <ronald.archlinux.org>
# Contributor: Damir Perisa <damir.perisa@bluewin.ch>
pkgname=stellarium
pkgver=24.3
pkgrel=2
pkgdesc="Software which renders realistic skies in real time with OpenGL"
arch=(x86_64)
url="https://${pkgname}.org"
license=(GPL-2.0-or-later)
depends=(nlopt libpng libglvnd freetype2 openssl gpsd calcmysky qt6-charts qt6-serialport
  qt6-multimedia qt6-positioning qt6-webengine qxlsx-qt6) # libindi
makedepends=(cmake ninja mesa qt6-tools)                  # doxygen graphviz
optdepends=('man-db: manual pages for stellarium')
source=(https://github.com/Stellarium/${pkgname}/releases/download/v${pkgver}/${pkgname}-${pkgver}.tar.gz{,.asc}
  onetbb-compatibility.patch::https://github.com/Stellarium/${pkgname}/commit/02e37f3b76ef20786f10a6d89d23944e330aecf4.patch)
validpgpkeys=('79151C2E6351E7278DA1A730BF38D4D02A328DFF') # Alexander Wolf <alex.v.wolf@gmail.com>
md5sums=('375367ffdfbbe3e4d4443ecebacf97ae'
  'SKIP'
  'be23a437a1584a5473aa1bc589b62151')
sha256sums=('c3ffb56a049061c7754bafab176146a2c4474ecede108d650f3c7551e1eae50a'
  'SKIP'
  '457cb3d27c46bf64be6dff930e31ba2d8ec14aeb2501c1d7135de9f7f5443353')

prepare() {
  cd ${pkgname}-${pkgver}
  # https://github.com/Stellarium/stellarium/issues/3905
  patch -p1 -i ../onetbb-compatibility.patch
}

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
