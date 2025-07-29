# Maintainer: KUHTOXO https://aur.archlinux.org/account/kuhtoxo
# Maintainer: Zoddo <archlinux+aur@zoddo.fr>
# Contributor: void09 <sgmihai at gmail dot com>
# Contributor: taotieren <admin@taotieren.com>
# Contributor: Leon Möller <jkhsjdhjs at totally dot rip>

pkgbase=rustdesk-bin
pkgname=(rustdesk-bin)
pkgver=1.4.1
pkgrel=3
pkgdesc="Yet another remote desktop software, written in Rust. Works out of the box, no configuration required."
url="https://github.com/rustdesk/rustdesk"
license=('AGPL-3.0-only')
arch=('x86_64' 'aarch64')
provides=("${pkgname%-bin}")
conflicts=("${pkgname%-bin}")
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
source_x86_64=("${pkgbase%-bin}-${pkgver}-${pkgrel}-x86_64.pkg.tar.zst::$url/releases/download/${pkgver/_/-}/rustdesk-${pkgver/_/-}-0-x86_64.pkg.tar.zst")
source_aarch64=("${pkgbase%-bin}-${pkgver}-${pkgrel}-aarch64.rpm::$url/releases/download/${pkgver/_/-}/rustdesk-${pkgver/_/-}-0.aarch64.rpm")
sha256sums_x86_64=('cb528ffe44601eaa76f250f5827243820d7bdb9d270dcadc8fcf62a05a4ad5b5')
sha256sums_aarch64=('f6ea58907555f4d06aea64261838e40e5c875f794ae84c6cb5ab94e89a82100e')

install=$pkgname.install

package() {
    install -d "${pkgdir}/usr/share/" "${pkgdir}/usr/bin/"
    cp -r "${srcdir}/usr/share/rustdesk/" "${pkgdir}/usr/share/"
    cp -r "${srcdir}/usr/share/icons/" "${pkgdir}/usr/share/"

    ln -s "/usr/share/rustdesk/rustdesk" "${pkgdir}/usr/bin/rustdesk"

    install -Dm 644 "${srcdir}/usr/share/rustdesk/files/rustdesk.service" "${pkgdir}/usr/lib/systemd/system/rustdesk.service"
    install -Dm 644 "${srcdir}/usr/share/rustdesk/files/rustdesk.desktop" "${pkgdir}/usr/share/applications/rustdesk.desktop"
    install -Dm 644 "${srcdir}/usr/share/rustdesk/files/rustdesk-link.desktop" "${pkgdir}/usr/share/applications/rustdesk-link.desktop"

    # Remove useless files
    rm -r "${pkgdir}/usr/share/rustdesk/files/"
}

