# Maintainer: KUHTOXO https://aur.archlinux.org/account/kuhtoxo
# Co-Maintainer: taotieren <admin@taotieren.com>
# Co-Maintainer: Leon Möller <jkhsjdhjs at totally dot rip>

pkgbase=rustdesk-bin
pkgname=(rustdesk-bin)
pkgver=1.3.0
pkgrel=1
pkgdesc="Yet another remote desktop software, written in Rust. Works out of the box, no configuration required."
url="https://github.com/rustdesk/rustdesk"
license=('AGPL-3.0')
arch=('x86_64')
provides=("${pkgname%-bin}")
conflicts=(
    'rustdesk'
    'rustdesk-git'
    'rustdesk-appimage-nightly'
    'rustdesk-nightly'
    'rustdesk-appimage'
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
sha256sums=('4b87ab3261d16ba0394e437fa867d102484c38975a213cfed1d028fe7b0fa51e')

install=$pkgname.install

package() {
    cp -r "$srcdir/usr/" "$pkgdir/usr/"
}