# Maintainer: nightuser <nightuser.android@gmail.com>

pkgname=glib2-static
pkgver=2.66.1
pkgrel=1
pkgdesc="Low level core library: Static library"
url="https://wiki.gnome.org/Projects/GLib"
license=(LGPL2.1)
arch=(x86_64)
depends=()
makedepends=(gettext zlib libffi shared-mime-info python libelf git util-linux meson dbus)
checkdepends=(desktop-file-utils)
options=('!docs' '!libtool' '!emptydirs' '!strip' 'staticlibs')
source=("http://ftp.gnome.org/pub/gnome/sources/glib/${pkgver%.*}/glib-$pkgver.tar.xz"
  '1683.patch')
sha256sums=('a269ffe69fbcc3a21ff1acb1b6146b2a5723499d6e2de33ae16ccb6d2438ef60'
  'e1913090c7cdd4c7db12651858a8381be28ae61f19d5e5e02a33f4c7c74c926d')

prepare() {
  cd "glib-$pkgver"
  patch -Np1 -i "$srcdir/1683.patch"
}

build() {
  CFLAGS+=' -Wno-unused-result'
  arch-meson "glib-$pkgver" _build \
    --default-library static \
    --buildtype release \
    -Dselinux=disabled \
    -Dman=false \
    -Dgtk_doc=false \
    -Dinternal_pcre=false
  ninja -C _build
}

check() {
  meson test -C _build --no-suite flaky --timeout-multiplier 2 --print-errorlogs
}

package() {
  DESTDIR="$pkgdir" meson install -C _build

  # Only install static library
  rm -rf "$pkgdir"/usr/{bin,include,share,lib/glib-2.0,lib/pkgconfig}
}

# vim: et:sw=2:ts=8
