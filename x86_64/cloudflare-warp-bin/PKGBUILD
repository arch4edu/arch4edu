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
pkgver=2026.8.2100.0
pkgrel=1
pkgdesc="Cloudflare Warp Client"
arch=('x86_64')
url="https://1.1.1.1"
license=('unknown')
depends=('at-spi2-core'
         'ayatana-ido'
         'cairo'
         'curl'
         'dbus'
         'fontconfig'
         'gdk-pixbuf2'
         'glib2'
         'glibc'
         'gtk3'
         'harfbuzz'
         'hicolor-icon-theme'
         'libayatana-appindicator'
         'libayatana-indicator'
         'libdbusmenu-glib'
         'libepoxy'
         'libgcc'
         'libsoup3'
         'libstdc++'
         'nftables'
         'nspr'
         'nss'
         'pango'
         'tpm2-tss'
         'webkit2gtk-4.1'
         'zlib')
makedepends=('chrpath')
provides=('warp-cli' 'warp-diag' 'warp-svc')
conflicts=("${pkgname%-bin}")
options=('!strip')
install="${pkgname}.install"
source=("${pkgname}-${pkgver}.deb::https://pkg.cloudflareclient.com/pool/resolute/main/c/cloudflare-warp/cloudflare-warp_${pkgver}_amd64.deb")
sha256sums=('28b8cf4c89084cf598065a328aef65e75af7fece382e38dd47a4c6caf1fca96b')

prepare() {
    mkdir -p build
    bsdtar -xzf data.tar.gz -C build

    sed -e "s%ExecStart=/bin/warp-svc%ExecStart=/usr/bin/warp-svc%" \
        -i build/lib/systemd/system/warp-svc.service
    sed -e "s%ExecStart=/bin/warp-taskbar%ExecStart=/usr/bin/warp-taskbar%" \
        -e "s%BindsTo=graphical-session.target%PartOf=graphical-session.target%" \
        -i build/usr/lib/systemd/user/warp-taskbar.service

    chrpath --delete build/usr/lib/warp/lib/{crashpad_handler,libdartjni.so}
    chrpath --replace /usr/lib/warp/lib build/usr/lib/warp/lib/*plugin.so
}

package() {
    cp -R build/{etc,usr} "${pkgdir}"
    cp -R build/{bin,lib} "${pkgdir}/usr"
}
