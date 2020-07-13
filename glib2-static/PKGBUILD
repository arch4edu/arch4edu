# Maintainer: nightuser <nightuser.android@gmail.com>

pkgname=glib2-static
pkgver=2.64.4
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
        'MR1405.patch'
        'MR1414.patch')
sha256sums=('f7e0b325b272281f0462e0f7fff25a833820cac19911ff677251daf6d87bce50'
            '934d87deaf597d7122f89d03c22b122a89eacbe46e887ce8e920a344926da2fb'
            '19cd43aa20962e2e27c55553b871ab1bb970289219545447887cc5e654245fed')

prepare() {
  cd "glib-$pkgver"

  patch -Np1 -i "$srcdir/MR1405.patch"
  patch -Np1 -i "$srcdir/MR1414.patch"
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
