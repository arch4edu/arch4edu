# Maintainer: Antonio Rojas <arojas@archlinux.org>
# Contributor: Eric Bélanger <eric@archlinux.org>

pkgname=wxwidgets-gtk2
pkgver=3.2.0
pkgrel=4
arch=(x86_64)
url='https://wxwidgets.org'
license=(custom:wxWindows)
makedepends=(cmake gst-plugins-base glu libnotify qt5-base sdl2 libmspack gtk2)
source=(https://github.com/wxWidgets/wxWidgets/releases/download/v$pkgver/wxWidgets-$pkgver.tar.bz2
        destdir.patch)
sha256sums=('356e9b55f1ae3d58ae1fed61478e9b754d46b820913e3bfbc971c50377c1903a'
            'cb4a7ca0d40b090d5d40d77790828a26766c6b496b3a5f5351fa30b3a6b42bd9')
options=(debug)

prepare() {
  patch -d wxWidgets-$pkgver -p1 < destdir.patch # Honor DESTDIR
}

build() {
  cmake -B build-gtk2 -S wxWidgets-$pkgver \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=None \
    -DwxBUILD_TOOLKIT=gtk2 \
    -DwxUSE_OPENGL=ON \
    -DwxUSE_REGEX=sys\
    -DwxUSE_ZLIB=sys \
    -DwxUSE_EXPAT=sys \
    -DwxUSE_LIBJPEG=sys \
    -DwxUSE_LIBPNG=sys \
    -DwxUSE_LIBTIFF=sys \
    -DwxUSE_LIBLZMA=sys \
    -DwxUSE_LIBMSPACK=ON \
    -DwxUSE_PRIVATE_FONTS=ON
  cmake --build build-gtk2
}

package_wxwidgets-gtk2() {
  pkgdesc='GTK+2 implementation of wxWidgets API for GUI'
  depends=(gtk2 gst-plugins-base-libs libsm wxwidgets-common libnotify libmspack sdl2)
  conflicts=(wxgtk wxgtk2)
  provides=(wxgtk wxgtk2 wxwidgets)

  DESTDIR="$pkgdir" cmake --install build-gtk2
  rm -r "$pkgdir"/usr/{include,lib/cmake,lib/libwx_base*,bin/wxrc*}
  mv "$pkgdir"/usr/bin/wx-config{,-gtk2} # Conflicts with wx-gtk3

  install -Dm644 wxWidgets-$pkgver/docs/licence.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
