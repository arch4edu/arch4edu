# Maintainer: sukanka<su975853527[AT]gmail.com>
# Contributor: Sam L. Yes <samlukeyes123 at gmail dot com>

_pkgname=wemeet
pkgname=$_pkgname-bin
provides=('wemeet' 'tencent-meeting')
pkgver=3.15.0.402
_pkgver_arm=${pkgver} # 两个版本有时候不一样
_x86_md5=22516e32c067130e73b91ea0793495ae
_arm_md5=9d3403df3db67092990ce8ad9438a53a
pkgrel=1
pkgdesc="Tencent Video Conferencing, tencent meeting 腾讯会议"
arch=('x86_64' 'aarch64')
license=('unknown')
url="https://source.meeting.qq.com/download-center.html"
source_x86_64=("${_pkgname}-${pkgver}-x86_64.deb::https://updatecdn.meeting.qq.com/cos/${_x86_md5}/TencentMeeting_0300000000_${pkgver}_x86_64_default.publish.deb"
)
source_aarch64=("${_pkgname}-${_pkgver_arm}-aarch64.deb::https://updatecdn.meeting.qq.com/cos/${_arm_md5}/TencentMeeting_0300000000_${_pkgver_arm}_arm64_default.publish.deb")
source=("${_pkgname}".sh 'wrap.c')
depends=('qt5-webengine' 'qt5-x11extras' 'libxinerama'
    'pulseaudio' # 无 pulseaudio 无法连接到系统音频
)
## 下面的库官方包有，但是 namcap 认为不需要，也没发现有什么影响
# 'qt5-base' 'hicolor-icon-theme'
# 'libbsd' 'flac' 'libidn11' 'libvorbis' 'libwrap'
# 'qt5-lottie' 'qt5-tools'  'qt5-networkauth' 'qt5-quickcontrols2'
# 'qt5-remoteobjects' 'qt5-script' 'qt5-scxml' 'qt5-svg'
# 'qt5-speech' 'qt5-wayland' 'qt5-websockets' 'qt5-webview' 'qt5-xmlpatterns'
optdepends=('bubblewrap: Fix abnormal text color in dark mode and prevent messing files.')
makedepends=('patchelf')
sha512sums=('e5b85510cebc3b73c65228feaa97a5bb3eb360ac467ef6cb8bdcde8e912819000b859b0e0fba8fa154272d613dc6541a9a29d64f56ecbb0877288d1de011029c'
            '48e40dfaf425f096802bfff081a9a1a3122f1f677227f1dbe67cfb37cef7ab8fe6060258161c79b07cd559c4022de6cea42245400ccfd1eac8456c7b42260550')
sha512sums_x86_64=('b01204b6452ac72a1fd09bded5ef48658e3995d9150d95b891a3d293afba8fa1f41b6866a08953ada8e1dd7c2094324f30d74ea87bf0770ed324f0f7f1f8383b')
sha512sums_aarch64=('6fe8708f3ff0233f393c03cf80dfae90d200da91f30d75592120f676218f808d0f7ea30b21133cbf4c7296fa6fd6b6d648ad30c2c699d0a0dfecc434e9c255e0')

prepare() {
    cd "$srcdir"
    tar xpf data.tar.xz

    pushd usr/share/applications
    sed -i 's|^Exec=.*|Exec=wemeet %u|g;s|^Icon=.*|Icon=wemeet|g' ${_pkgname}app.desktop
    sed -i '$i Comment=Tencent Meeting Linux Client\nComment[zh_CN]=腾讯会议Linux客户端\nKeywords=wemeet;tencent;meeting;' \
        "$srcdir/usr/share/applications/wemeetapp.desktop"
    popd

    pushd opt/$_pkgname
    for res in 16 32 64 128 256; do
        install -dm755 "$srcdir/usr/share/icons/hicolor/${res}x${res}/apps"
        mv "icons/hicolor/${res}x${res}/mimetypes/${_pkgname}app.png" \
            "$srcdir/usr/share/icons/hicolor/${res}x${res}/apps/${_pkgname}app.png"
    done

    rm bin/qt.conf
    patchelf --set-rpath /usr/lib/$_pkgname bin/wemeetapp
    popd

    pushd opt/$_pkgname/bin
    rm Qt*
    for dir in modules/*; do
        patchelf --set-rpath '$ORIGIN:/usr/lib/wemeet' "$dir"/*.so
    done
    popd
}

build() {
    cd "$srcdir"
    read -ra openssl_args < <(pkgconf --libs openssl)
    read -ra libpulse_args < <(pkgconf --cflags --libs libpulse)
    # Comment out `-D WRAP_FORCE_SINK_HARDWARE` to disable the patch that forces wemeet detects sink as hardware sink
    "${CC:-cc}" $CFLAGS -fPIC -shared "${openssl_args[@]}" "${libpulse_args[@]}" -o libwemeetwrap.so wrap.c -D WRAP_FORCE_SINK_HARDWARE
}

package() {
    cd "$srcdir"
    cp -r usr "$pkgdir"
    cd opt/$_pkgname

    install -Dm755 "$srcdir/$_pkgname.sh" "$pkgdir/usr/bin/$_pkgname"
    install -Dm644 $_pkgname.svg -t "$pkgdir/usr/share/icons/hicolor/scalable/apps"

    install -Dm755 lib/lib{bugly,crbase,desktop_common,ImSDK,nxui*,qt_*,service*,tms_*,ui*,wemeet*,xcast*,xnn*}.so \
        -t "$pkgdir/usr/lib/$_pkgname"
    for lib in "$pkgdir/usr/lib/$_pkgname"/*; do
        patchelf --set-rpath '$ORIGIN' "$lib"
    done

    install -dm755 "$pkgdir/opt/$_pkgname"
    cp -r bin "$pkgdir/opt/$_pkgname"
    ln -s raw/xcast.conf "$pkgdir/opt/$_pkgname/bin/xcast.conf"
    install -Dm755 "$srcdir/libwemeetwrap.so" -t "$pkgdir/usr/lib/$_pkgname"
}
