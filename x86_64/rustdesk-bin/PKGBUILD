# Maintainer: KUHTOXO https://aur.archlinux.org/account/kuhtoxo
# Maintainer: Zoddo <archlinux+aur@zoddo.fr>
# Contributor: void09 <sgmihai at gmail dot com>
# Contributor: taotieren <admin@taotieren.com>
# Contributor: Leon Möller <jkhsjdhjs at totally dot rip>

pkgbase=rustdesk-bin
pkgname=(rustdesk-bin)
pkgver=1.3.5
pkgrel=1
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
source_x86_64=("${pkgbase%-bin}-${pkgver}-x86_64.pkg.tar.zst::$url/releases/download/${pkgver/_/-}/rustdesk-${pkgver/_/-}-0-x86_64.pkg.tar.zst")
source_aarch64=("${pkgbase%-bin}-${pkgver}-aarch64.rpm::$url/releases/download/${pkgver/_/-}/rustdesk-${pkgver/_/-}-0.aarch64.rpm")
sha256sums_x86_64=('19359ee25ffd0ea92e1f8f0cbbdfe181ab24b9acef0cd3907b46324acea2466c')
sha256sums_aarch64=('b25075684a0471a42cd1c8403b71cdd61e623956d6fdbce84ded03244a5d2410')

install=$pkgname.install

package() {
    install -d "${pkgdir}/usr/lib/" "${pkgdir}/usr/share/" "${pkgdir}/usr/bin/"
    cp -r "${srcdir}/usr/lib/rustdesk/" "${pkgdir}/usr/lib/"
    cp -r "${srcdir}/usr/share/icons/" "${pkgdir}/usr/share/"

    ln -s "/usr/lib/rustdesk/rustdesk" "${pkgdir}/usr/bin/rustdesk"

    install -Dm 644 "${srcdir}/usr/share/rustdesk/files/rustdesk.service" "${pkgdir}/usr/lib/systemd/system/rustdesk.service"

    # Desktop files are renamed to prevent conflict with manually installed (non pacman-tracked) files between 1.3.0-2 and 1.3.1-0.
    # Old files will be cleaned by the .INSTALL pre_upgrade() script. I believe we can revert to normal file names when some time will have passed.
    # -- Zoddo, 2024-09-23
    install -Dm 644 "${srcdir}/usr/share/rustdesk/files/rustdesk.desktop" "${pkgdir}/usr/share/applications/rustdesk-bin.desktop"
    install -Dm 644 "${srcdir}/usr/share/rustdesk/files/rustdesk-link.desktop" "${pkgdir}/usr/share/applications/rustdesk-bin-link.desktop"
    sed -i '/StartupNotify=true/a StartupWMClass=rustdesk' "${pkgdir}/usr/share/applications/rustdesk-bin.desktop" # Temporarily needed while the filename doesn't match the WM_CLASS
}

