# Maintainer: Qirui Wang <wqr.prg@gmail.com>

pkgbase=wxgtk-dev
pkgname=(wxgtk2-dev wxgtk3-dev wxgtk-common-dev)
pkgver=3.1.7
pkgrel=1
arch=('x86_64')
url="https://wxwidgets.org"
license=('custom:wxWindows')
makedepends=('gst-plugins-base' 'glu' 'webkit2gtk' 'libnotify' 'gtk2')
options=('!emptydirs')
source=("https://github.com/wxWidgets/wxWidgets/releases/download/v${pkgver}/wxWidgets-${pkgver}.tar.bz2")
sha1sums=('893e7886bc1e9fcf691bd4db0c9e49dc8413f674')
sha256sums=('3d666e47d86192f085c84089b850c90db7a73a5d26b684b617298d89dce84f19')

prepare() {
  cp -a wxWidgets-${pkgver} wxWidgets-${pkgver}-gtk2
}

build() {
  cd wxWidgets-${pkgver}
  ./configure --prefix=/usr --libdir=/usr/lib --with-gtk=3 --with-opengl --enable-unicode \
    --enable-graphics_ctx --enable-mediactrl --enable-webview --with-regex=builtin \
    --with-libpng=sys --with-libxpm=sys --with-libjpeg=sys --with-libtiff=sys \
    --disable-precomp-headers
  make
  make -C locale allmo

  cd ../wxWidgets-${pkgver}-gtk2
  ./configure --prefix=/usr --libdir=/usr/lib --with-gtk=2 --with-opengl --enable-unicode \
    --enable-graphics_ctx --enable-mediactrl --with-regex=builtin \
    --with-libpng=sys --with-libxpm=sys --with-libjpeg=sys --with-libtiff=sys \
    --disable-precomp-headers
  make
}

package_wxgtk-common-dev() {
  pkgdesc='Common libraries and headers for wxgtk2 and wxgtk3'
  depends=('zlib' 'gcc-libs' 'expat')
  conflicts=('wxgtk-common')
  provides=('wxgtk-common')

  cd wxWidgets-${pkgver}
  make DESTDIR="${pkgdir}" install
  rm -r "$pkgdir"/usr/{bin/wx-config,lib/{wx,libwx_gtk*}}

  install -D -m644 docs/licence.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_wxgtk2-dev() {
  pkgdesc='GTK+2 implementation of wxWidgets API for GUI'
  depends=('gtk2' 'libgl' 'gst-plugins-base-libs' 'libsm' 'libxxf86vm' 'wxgtk-common-dev' 'libnotify')
  conflicts=('wxgtk' 'wxgtk2')
  provides=('wxgtk' 'wxgtk2')
  replaces=('wxgtk')

  cd wxWidgets-${pkgver}-gtk2
  make DESTDIR="${pkgdir}" install
  rm -r "$pkgdir"/usr/{include,share,lib/libwx_base*,bin/wxrc*}
  mv "$pkgdir"/usr/bin/wx-config{,-gtk2}
  
  install -D -m644 docs/licence.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_wxgtk3-dev() {
  pkgdesc='GTK+3 implementation of wxWidgets API for GUI'
  depends=('gtk3' 'gst-plugins-base-libs' 'libsm' 'libxxf86vm' 'wxgtk-common-dev' 'libnotify')
  optdepends=('webkit2gtk: for webview support')
  conflicts=('wxgtk<3.0.3.1-2' 'wxgtk3')
  provides=('wxgtk3')

  cd wxWidgets-${pkgver}
  make DESTDIR="${pkgdir}" install  
  rm -r "$pkgdir"/usr/{include,share,lib/libwx_base*,bin/wxrc*}
  ln -s wx-config "$pkgdir"/usr/bin/wx-config-gtk3
   
  install -D -m644 docs/licence.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
