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
pkgver=2024.11.309
pkgrel=1
pkgdesc="Cloudflare Warp Client"
arch=('x86_64')
url="https://1.1.1.1"
license=('unknown')
depends=('cairo'
         'dbus'
         'gcc-libs'
         'gdk-pixbuf2'
         'glib2'
         'glibc'
         'gtk3'
         'hicolor-icon-theme'
         'nspr'
         'nss'
         'pango')
provides=('warp-cli' 'warp-diag' 'warp-svc')
conflicts=("${pkgname%-bin}")
source=("${pkgname}-${pkgver}.deb::https://pkg.cloudflareclient.com/pool/noble/main/c/cloudflare-warp/cloudflare-warp_${pkgver}.0_amd64.deb")
sha256sums=('4c7c57113cb2d3cac19af821adcf07210d9c0522de35597c4a40f8dc2558fed1')

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
        -i "${pkgdir}/usr/lib/systemd/user/warp-taskbar.service"
}
