# Maintainer: KUHTOXO https://aur.archlinux.org/account/kuhtoxo
# Maintainer: Zoddo <archlinux+aur@zoddo.fr>
# Contributor: taotieren <admin@taotieren.com>
# Contributor: Leon Möller <jkhsjdhjs at totally dot rip>

pkgbase=rustdesk-appimage
pkgname=(rustdesk-appimage)
pkgver=1.4.8
pkgrel=1
pkgdesc="Yet another remote desktop software, written in Rust. Works out of the box, no configuration required."
url="https://github.com/rustdesk/rustdesk"
license=('AGPL-3.0-only')
arch=('x86_64' 'aarch64')
provides=("${pkgname%-appimage}")
conflicts=("${pkgname%-appimage}")
optdepends=(
    'libappindicator-gtk3: tray icon'
    'libayatana-appindicator: tray icon'
)
options=('!strip')
source_x86_64=("${pkgbase%-appimage}-${pkgver}-${pkgrel}-x86_64.AppImage::${url}/releases/download/${pkgver}/${pkgbase%-appimage}-${pkgver}-x86_64.AppImage")
source_aarch64=("${pkgbase%-appimage}-${pkgver}-${pkgrel}-aarch64.AppImage::${url}/releases/download/${pkgver}/${pkgbase%-appimage}-${pkgver}-aarch64.AppImage")
sha256sums_x86_64=('ae1ec1a6f4f92da41acad6d166a362bd39bbbd02bb70265641558696c2509ccb')
sha256sums_aarch64=('b9ee9394b5181c45f851e79cc0471eafdcedf611ce20f64ac7c9af9276671ef0')
_install_path="/opt/appimages"

prepare() {
    cd ${srcdir}
    chmod a+x ${pkgbase%-appimage}-${pkgver}-${pkgrel}-${CARCH}.AppImage
    "./${pkgbase%-appimage}-${pkgver}-${pkgrel}-${CARCH}.AppImage" --appimage-extract > /dev/null
    sed 's|usr/share/rustdesk/rustdesk|/opt/appimages/rustdesk.AppImage|g' -i "${srcdir}/squashfs-root/${pkgbase%-appimage}.desktop"
}

package() {
    install -Dm755 "${srcdir}"/${pkgbase%-appimage}-${pkgver}-${pkgrel}-${CARCH}.AppImage "${pkgdir}"/${_install_path}/${pkgbase%-appimage}.AppImage

    local _icon
    for _icon in 32 64 128 ; do
        install -Dm0644 "${srcdir}/squashfs-root/usr/share/icons/hicolor/${_icon}x${_icon}/apps/${pkgbase%-appimage}.png" \
                    -t  "${pkgdir}/usr/share/icons/hicolor/${_icon}x${_icon}/apps"
    done

    install -Dm644 "${srcdir}/squashfs-root/${pkgbase%-appimage}.desktop" -t "${pkgdir}/usr/share/applications"
}
