# Maintainer: Leon Mergen <leon@solatis.com>
# Maintainer: Mahdi Sarikhani <mahdisarikhani@outlook.com>
# Maintainer: Noah Kennedy <nomaxx117@gmail.com>
# Maintainer: Riichi Rusdiana <contact@riichi.my.id>
# Contributor: unlogicalcode <jearsmail99@gmail.com>
# Contributor: Arsalan Rezazadeh <arsalanrezazadeh4@gmail.com>
# Contributor: Jongsik Kim <jjong84@gmail.com>
# Contributor: <memoryshadow@outlook.com>
# Contributor: Daffa Haj Tsaqif <narutohaj00@gmail.com>

pkgname=cloudflare-warp-bin
pkgver=2026.1.150
pkgrel=1
pkgdesc="Cloudflare Warp Client"
arch=('x86_64')
url="https://1.1.1.1"
license=('unknown')
depends=('dbus'
         'glib2'
         'glibc'
         'gtk3'
         'hicolor-icon-theme'
         'libgcc'
         'nftables'
         'nspr'
         'nss')
provides=('warp-cli' 'warp-diag' 'warp-svc')
conflicts=("${pkgname%-bin}")
install="${pkgname}.install"
source=("${pkgname}-${pkgver}.deb::https://pkg.cloudflareclient.com/pool/noble/main/c/cloudflare-warp/cloudflare-warp_${pkgver}.0_amd64.deb")
sha256sums=('2e388e4746e2cb1918227f84da38786de3dded883feaa3ad4fb5be10a70bc30a')

prepare() {
    mkdir -p "${srcdir}/build"
    bsdtar -xzf data.tar.gz -C "${srcdir}/build"
}

package() {
    cp -R "${srcdir}/build/"{etc,usr} "${pkgdir}"
    cp -R "${srcdir}/build/"{bin,lib} "${pkgdir}/usr"

    sed -e "s%ExecStart=/bin/warp-svc%ExecStart=/usr/bin/warp-svc%" \
        -i "${pkgdir}/usr/lib/systemd/system/warp-svc.service"
    sed -e "s%ExecStart=/bin/warp-taskbar%ExecStart=/usr/bin/warp-taskbar%" \
        -e "s%BindsTo=graphical-session.target%PartOf=graphical-session.target%" \
        -i "${pkgdir}/usr/lib/systemd/user/warp-taskbar.service"
}
