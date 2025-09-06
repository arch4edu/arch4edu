# Maintainer: shmilee <shmilee.zju at gmail dot com>
# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>
# Contributor: mcmillan <awmcmillan at gmail dot com>

_pkgbase='engauge-digitizer'

pkgname=('engauge' 'engauge-samples')
pkgbase='engauge'
pkgver=12.9.1
pkgrel=2
epoch=1
url="https://akhuettel.github.io/engauge-digitizer"
arch=('i686' 'x86_64')
license=('GPL-2')
makedepends=('qt6-tools' 'fftw' 'libjpeg-turbo' 'libpng' 'openjpeg2' 'poppler-qt6')
source=("$pkgbase-$pkgver.tar.gz::https://github.com/akhuettel/$_pkgbase/archive/v$pkgver.tar.gz"
        "$pkgbase.sh"
        "$pkgbase.desktop")
sha256sums=('0da5d884390af70770204a0c19e3b1e2fca876ba1d5f416b62a6922edff365f3'
            '4b36a8aa23c5a95a552d33ce1bd75aa1a0be5fdf9ef06f321a060c753298dd18'
            '1b3f2675058693d5653b5aee50fbec1530791de5fcdfbb2f86056a5d748695a4')
install=engauge.install
options=(!debug)

build() {
  cd ${_pkgbase}-$pkgver
  export OPENJPEG_INCLUDE=$(pkg-config --variable includedir libopenjp2) OPENJPEG_LIB=/usr/lib
  export POPPLER_INCLUDE=$(pkg-config --cflags-only-I poppler-qt6 | cut -d ' ' -f 1 | sed 's/^-I//') POPPLER_LIB=/usr/lib

  # This otherwise overrides user CFLAGS
  sed -e '/QMAKE_CXXFLAGS_WARN_ON/s/-O1//' \
    -i engauge.pro

  qmake6 engauge.pro "CONFIG+=pdf jpeg2000 log4cpp_null"
  make
  /usr/lib/qt6/bin/lrelease engauge.pro
  cd help/
  sed -e 's|^qhelpgenerator engauge.qhp|/usr/lib/qt6/qhelpgenerator engauge.qhp engauge.qhcp|' \
      -i ./build.bash
  ./build.bash
}

package_engauge() {
  pkgdesc="Extracts data points from images of graphs"
  depends=('qt6-tools' 'fftw' 'libjpeg-turbo' 'libpng' 'openjpeg2' 'poppler-qt6')

  cd ${_pkgbase}-$pkgver
  install -Dm755 ../$pkgbase.sh "$pkgdir"/usr/bin/$pkgbase
  install -Dm755 bin/Engauge "$pkgdir"/usr/lib/$_pkgbase/$pkgbase
  # translations
  install -dm755 "$pkgdir"/usr/lib/$_pkgbase/translations/
  install -Dm64 translations/*.qm -t "$pkgdir"/usr/lib/$_pkgbase/translations/
  # help
  install -Dm644 bin/documentation/engauge.qch \
    "$pkgdir/usr/share/doc/$_pkgbase/engauge.qch"
  install -Dm644 bin/documentation/engauge.qhc \
    "$pkgdir/usr/share/doc/$_pkgbase/engauge.qhc"
  # icon
  install -Dm644 src/img/$_pkgbase.svg \
    "$pkgdir"/usr/share/icons/$_pkgbase.svg
  # desktop
  install -Dm644 "$srcdir"/${pkgbase%-git}.desktop \
	  "$pkgdir"/usr/share/applications/${pkgbase%-git}.desktop
}

package_engauge-samples() {
  pkgdesc="sample image files for engauge copied into the doc subdirectory"
  arch=('any')

  cd ${_pkgbase}-$pkgver
  install -d "$pkgdir"/usr/share/doc/$_pkgbase
  cp -r samples "$pkgdir"/usr/share/doc/$_pkgbase/
}
