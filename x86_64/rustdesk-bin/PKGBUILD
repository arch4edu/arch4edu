# Maintainer: KUHTOXO https://aur.archlinux.org/account/kuhtoxo
# Co-Maintainer: taotieren <admin@taotieren.com>
# Co-Maintainer: Leon Möller <jkhsjdhjs at totally dot rip>

pkgbase=rustdesk-bin
pkgname=(rustdesk-bin)
pkgver=1.3.1
pkgrel=0
pkgdesc="Yet another remote desktop software, written in Rust. Works out of the box, no configuration required."
url="https://github.com/rustdesk/rustdesk"
license=('AGPL-3.0')
arch=('x86_64')
provides=("${pkgname%-bin}")
conflicts=(
    'rustdesk'
)
depends=(
    'gtk3'
    'xdotool'
    'libxcb'
    'libxfixes'
    'alsa-lib'
    'libva'
    'libvdpau'
    'pam'
    'gst-plugins-base'
    'gst-plugin-pipewire'
)
optdepends=(
    'libappindicator-gtk3: tray icon'
    'libayatana-appindicator: tray icon'
)
options=('!strip' '!lto' '!debug')
source=("${pkgbase%-bin}-${pkgver}-$CARCH.pkg.tar.zst::$url/releases/download/${pkgver/_/-}/rustdesk-${pkgver/_/-}-0-$CARCH.pkg.tar.zst")
sha256sums=('ff95175843e3594dc3bc62924ea03782beff4d977529ca5db66d4c1c26477731')

install=$pkgname.install

package() {
    cp -r "$srcdir/usr/" "$pkgdir/usr/"
    mkdir -p $pkgdir/usr/lib/systemd/system/
    cp $srcdir/usr/share/rustdesk/files/rustdesk.service $pkgdir/usr/lib/systemd/system/rustdesk.service
    mkdir -p $pkgdir/usr/share/applications/
    cp $srcdir/usr/share/rustdesk/files/rustdesk.desktop $pkgdir/usr/share/applications/
    cp $srcdir/usr/share/rustdesk/files/rustdesk-link.desktop $pkgdir/usr/share/applications/
}