# Maintainer: taotieren <admin@taotieren.com>

pkgbase=ttf-misans
pkgname=($pkgbase)
pkgver=2.000
pkgrel=1
arch=(any)
url='https://web.vip.miui.com/page/info/mio/mio/detail?postId=33935854'
license=(custom)
#provides=()
#conflicts=()
depends=('fontconfig')
makedepends=()

source=("https://cdn.cnbj1.fds.api.mi-img.com/vipmlmodel/font/MiSans/MiSans.zip")

sha256sums=('38bdec9525024ee9ce1ee56ebc5a32a37efaecf86b385ec3da71898708dad7f6')

package_ttf-misans() {
    export LC_CTYPE="zh_CN.UTF-8"
    pkgdesc="MiSans MIUI 13 全新系统字体供全社会免费商用。"
    install -dm755 "${pkgdir}/usr/share/fonts/misans"

    cp -rv "${srcdir}"/MiSans\ 开发下载字重/*.ttf "${pkgdir}/usr/share/fonts/misans"
}

# vim: ts=4 sw=4 et
