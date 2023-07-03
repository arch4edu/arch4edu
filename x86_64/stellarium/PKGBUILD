# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Ronald van Haren <ronald.archlinux.org>
# Contributor: Damir Perisa <damir.perisa@bluewin.ch>

pkgname=stellarium
pkgver=23.2
pkgrel=1
pkgdesc="Software which renders realistic skies in real time with OpenGL"
arch=(x86_64)
url="https://${pkgname}.org"
license=(GPL2)
depends=('libpng' 'libglvnd' 'freetype2' 'openssl' 'gpsd' 'calcmysky'
  'qt6-charts' 'qt6-serialport' 'qt6-multimedia' 'qt6-positioning' 'qt6-webengine' 'libindi') # 'qxlsx-qt6'
makedepends=('cmake' 'ninja' 'mesa' 'qt6-tools')                                              # 'doxygen' 'graphviz'
optdepends=('man-db: manual pages for stellarium')
source=(https://github.com/Stellarium/${pkgname}/releases/download/v${pkgver}/${pkgname}-${pkgver}.tar.gz{,.asc}
  indi-2.0.patch::https://github.com/Stellarium/${pkgname}/pull/3269.patch)
validpgpkeys=('79151C2E6351E7278DA1A730BF38D4D02A328DFF') # Alexander Wolf <alex.v.wolf@gmail.com>
md5sums=('b42a829ffe080ba7c27b8ff25ba8a9c8'
  'SKIP'
  'c7dc3c0de63fc38136c96d1ce039483a')
sha256sums=('01bf23f7ff007c58b91bffe233938e2cf23e9182bd36bfe72715fbfbde57ec0a'
  'SKIP'
  '31c4024074705d5abe1236fa5a735c8d20fddc2d07a02603cb4600ce00cb5a63')

prepare() {
  # FIXME: https://github.com/Stellarium/stellarium/issues/3132#issuecomment-1485304021
  # sed -i 's/SOURCE_SUBDIR QXlsx/SOURCE_SUBDIR QXlsxQt${QT_VERSION_MAJOR}/' ${pkgname}-${pkgver}/CMakeLists.txt
  # TODO: https://github.com/Stellarium/stellarium/issues/3038
  cd ${pkgname}-${pkgver}
  patch -p1 -i ../indi-2.0.patch
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
    -DENABLE_XLSX=0 \
    -DPREFER_SYSTEM_INDILIB=Yes \
    -Wno-dev
  cmake --build build --target all
}

package() {
  DESTDIR="${pkgdir}" cmake --build build --target install
  install -Dm 644 ${pkgname}-${pkgver}/COPYING -t "${pkgdir}/usr/share/licenses/${pkgname}"
  find "${pkgdir}" -type d -empty -delete
}
