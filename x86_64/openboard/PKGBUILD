# Maintainer: Frank Siegert <frank.siegert@googlemail.com>
# Maintainer: Vekhir <vekhir at yahoo dot com>
# Contributor: bartus <arch-user-repoᘓbartus.33mail.com>

## Configuration env vars:
((ENABLE_QT5)) && QT_VER="5" || QT_VER="6"
qt="qt${QT_VER}"

pkgname=openboard
pkgver=1.7.3
_src_folder="OpenBoard-${pkgver}"
pkgrel=1
pkgdesc="Interactive whiteboard software for schools and universities"
arch=('x86_64' 'i686')
url="http://openboard.ch/index.en.html"
license=('GPL3')
# qt{5,6} libraries probed with `ldd -r /opt/openboard/OpenBoard` for both builds
#             qt5-base qt5-declarative qt5-location qt5-multimedia                 qt5-svg qt5-webchannel qt5-webengine
# qt6-5compat qt6-base qt6-declarative              qt6-multimedia qt6-positioning qt6-svg qt6-webchannel qt6-webengine
depends+=(${qt}-{base,declarative,multimedia,svg,webchannel,webengine})
depends+=('openssl' 'ffmpeg')
depends+=(quazip-${qt})  #drop internal quazip and use system one.
depends+=(poppler) #replace internal xpdf with poppler and drop freetype/xpdf from deps
makedepends=('cmake' ${qt}-tools)
source=("https://github.com/OpenBoard-org/OpenBoard/archive/v${pkgver}.tar.gz")
sha256sums=('55532df042e3a5b36e1f6f1e29916d3bbd01796d920782fa1f8a03438dcddd9c')

build() {
  cmake -B build -S "$srcdir"/$_src_folder \
    -DCMAKE_BUILD_TYPE=None \
    -DQT_VERSION=${QT_VER} \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DCMAKE_CXX_STANDARD=20 \
    -Wno-dev
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
