# Maintainer: taotieren <admin@taotieren.com>
# Co-Maintainer: Leon Möller <jkhsjdhjs at totally dot rip>

pkgbase=rustdesk-bin
pkgname=(rustdesk-bin)
pkgver=1.2.7
pkgrel=1
pkgdesc="Yet another remote desktop software, written in Rust. Works out of the box, no configuration required. Great alternative to TeamViewer and AnyDesk!"
url="https://github.com/rustdesk/rustdesk"
license=('GPL3')
arch=('x86_64')
provides=("${pkgname%-bin}")
conflicts=("${pkgname%-bin}")
depends=(
    'at-spi2-core'
    'cairo'
    'dbus'
    'fontconfig'
    'gcc-libs'
    'gdk-pixbuf2'
    'glib2'
    'glibc'
    'gstreamer'
    'gst-plugins-base-libs'
    'gtk3'
    'libepoxy'
    'libpulse'
    'libva'
    'libvdpau'
    'libx11'
    'libxcb'
    'libxkbcommon'
    'libxfixes'
    'libxtst'
    'pango'
    'pam'
    'xdotool'
    'hicolor-icon-theme'
)
optdepends=(
    'libappindicator-gtk3: tray icon'
    'libayatana-appindicator: tray icon'
)
options=('!strip' '!lto' '!debug')
source=("${pkgbase%-bin}-${pkgver}-$CARCH.pkg.tar.zst::$url/releases/download/${pkgver/_/-}/rustdesk-${pkgver/_/-}-0-$CARCH.pkg.tar.zst")
sha256sums=('SKIP')

prepare() {
    sed -i "s/^\(Icon=\).*$/\1rustdesk/" "$srcdir/usr/share/rustdesk/files/rustdesk.desktop"
}

package() {
# TODO: add dep on libsciter-gtk, remove libsciter-gtk.so from this package

    mkdir -p "$pkgdir/usr/bin/"
    ln -s "/usr/lib/rustdesk/rustdesk" "$pkgdir/usr/bin/rustdesk"

    mkdir -p "$pkgdir/usr/lib/"
    cp -r "$srcdir/usr/lib/rustdesk/" "$pkgdir/usr/lib/"

    install -Dm644 "$srcdir/usr/share/icons/hicolor/256x256/apps/rustdesk.png" "$pkgdir/usr/share/icons/hicolor/256x256/apps/rustdesk.png"
    install -Dm644 "$srcdir/usr/share/icons/hicolor/scalable/apps/rustdesk.svg" "$pkgdir/usr/share/icons/hicolor/scalable/apps/rustdesk.svg"
    install -Dm644 "$srcdir/usr/share/rustdesk/files/rustdesk.desktop" "$pkgdir/usr/share/applications/rustdesk.desktop"
    install -Dm644 "$srcdir/usr/share/rustdesk/files/rustdesk-link.desktop" "$pkgdir/usr/share/applications/rustdesk-link.desktop"
    install -Dm644 "$srcdir/usr/share/rustdesk/files/rustdesk.service" "$pkgdir/usr/lib/systemd/system/rustdesk.service"
}
