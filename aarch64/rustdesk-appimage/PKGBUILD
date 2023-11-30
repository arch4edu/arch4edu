# Maintainer: taotieren <admin@taotieren.com>
# Co-Maintainer: Leon Möller <jkhsjdhjs at totally dot rip>

pkgbase=rustdesk-appimage
pkgname=(rustdesk-appimage)
pkgver=1.2.3
pkgrel=0
pkgdesc="Yet another remote desktop software, written in Rust. Works out of the box, no configuration required. Great alternative to TeamViewer and AnyDesk! (AppImage)"
url="https://github.com/rustdesk/rustdesk"
license=('GPL3')
arch=('x86_64' 'aarch64')
provides=("${pkgname%-appimage}")
conflicts=("${pkgname%-appimage}")
optdepends=(
    'libappindicator-gtk3: tray icon'
    'libayatana-appindicator: tray icon'
)
options=('!strip')
source_x86_64=("${pkgbase%-appimage}-${pkgver}-x86_64.AppImage::${url}/releases/download/${pkgver}/${pkgbase%-appimage}-${pkgver}-x86_64.AppImage")
source_aarch64=("${pkgbase%-appimage}-${pkgver}-aarch64.AppImage::${url}/releases/download/${pkgver}/${pkgbase%-appimage}-${pkgver}-aarch64.AppImage")
sha256sums_x86_64=('SKIP')
sha256sums_aarch64=('SKIP')
_install_path="/opt/appimages"

prepare() {
    cd ${srcdir}
    chmod a+x ${pkgbase%-appimage}-${pkgver}-${CARCH}.AppImage
    "./${pkgbase%-appimage}-${pkgver}-${CARCH}.AppImage" --appimage-extract > /dev/null
    sed 's|usr/lib/rustdesk/rustdesk|/opt/appimages/rustdesk.AppImage|g' -i "${srcdir}/squashfs-root/${pkgbase%-appimage}.desktop"
}

package() {
    install -Dm755 "${srcdir}"/${pkgbase%-appimage}-${pkgver}-${CARCH}.AppImage "${pkgdir}"/${_install_path}/${pkgbase%-appimage}.AppImage

    local _icon
    for _icon in 32 64 128 ; do
        install -Dm0644 "${srcdir}/squashfs-root/usr/share/icons/hicolor/${_icon}x${_icon}/apps/${pkgbase%-appimage}.png" \
                    -t  "${pkgdir}/usr/share/icons/hicolor/${_icon}x${_icon}/apps"
    done

    install -Dm644 "${srcdir}/squashfs-root/${pkgbase%-appimage}.desktop" -t "${pkgdir}/usr/share/applications"
}
