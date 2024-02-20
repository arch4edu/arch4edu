# Maintainer: sukanka<su975853527[AT]gmail.com>
# Contributor: Sam L. Yes <samlukeyes123 at gmail dot com>

_pkgname=wemeet
pkgname=$_pkgname-bin
provides=('wemeet' 'tencent-meeting')
pkgver=3.19.0.401
_pkgver_arm=${pkgver} # 两个版本有时候不一样
_x86_md5=bb4001c715553579a8b3e496233331d4
_arm_md5=0f96a97b0aaea9b9d5d2c2b912ede656
pkgrel=3
pkgdesc="Tencent Video Conferencing, tencent meeting 腾讯会议"
arch=('x86_64' 'aarch64')
license=('unknown')
url="https://source.meeting.qq.com/download-center.html"
source_x86_64=("${_pkgname}-${pkgver}-x86_64.deb::https://updatecdn.meeting.qq.com/cos/${_x86_md5}/TencentMeeting_0300000000_${pkgver}_x86_64_default.publish.deb"
)
source_aarch64=("${_pkgname}-${_pkgver_arm}-aarch64.deb::https://updatecdn.meeting.qq.com/cos/${_arm_md5}/TencentMeeting_0300000000_${_pkgver_arm}_arm64_default.publish.deb")
source=("${_pkgname}".sh 'wrap.c')
depends=(
    bash
    qt5-webengine qt5-x11extras libxinerama
    libpulse # 无 pulseaudio 无法连接到系统音频
    # dependencies detected by namcap
    gcc-libs qt5-declarative libglvnd libxfixes alsa-lib qt5-webchannel openssl
    libxrandr libxext libx11 hicolor-icon-theme glibc zlib libxcomposite
    qt5-base systemd-libs libxdamage qt5-svg
)
optdepends=(
    'qt5-wayland: Wayland support'
    'bubblewrap: Fix abnormal text color in dark mode and prevent messing files.'
)
makedepends=('patchelf')
sha512sums=('86fad230304c9d12fc3c34635e4afb4eed5419298f1e357192ebd36953c273aae78f1c89587200e6ebeb374fec23f0486222a2ea86a73f9b72cf06d4628b587f'
            'f98e9ae5842c05a19ad4f883c8f9d88ef3b64e04b034e7fd8b23ddca81510f0bd38688ad7c63ddf8badaa727a7b599ceede87419e9694c06d7a4b06138b94c15')
sha512sums_x86_64=('2814febb1596cb8e6db75a7d71915771a9d6750cf162c3cb9b70379130da41d7fca7b3df1567a8de1d2967d97add4d2fc08764fbf4155a79852c75ea8fed754b')
sha512sums_aarch64=('6099ec383e74dc776a9864743c9a2c624a5bea34e2ffb32b3fb57b66016a60dc1356ad3b58c6142ed2f3d9db83fc38ffd9c9661b282bf895e20d837277a07c76')

prepare() {
    cd "$srcdir"
    tar xpf data.tar.xz

    pushd usr/share/applications
    # 暂时使用 x11, wayland 无法开启会议
    sed -i 's|^Exec=.*|Exec=wemeet-x11 %u|g;s|^Icon=.*|Icon=wemeet|g' ${_pkgname}app.desktop
    sed -i '$i Comment=Tencent Meeting Linux Client\nComment[zh_CN]=腾讯会议Linux客户端\nKeywords=wemeet;tencent;meeting;' \
        "$srcdir/usr/share/applications/wemeetapp.desktop"
    popd

    pushd opt/$_pkgname
    if [ -d 'icons' ]; then
        for res in 16 32 64 128 256; do
            install -dm755 "$srcdir/usr/share/icons/hicolor/${res}x${res}/apps"
            mv "icons/hicolor/${res}x${res}/mimetypes/${_pkgname}app.png" \
                "$srcdir/usr/share/icons/hicolor/${res}x${res}/apps/${_pkgname}app.png"
        done
    else
        echo 'icons directory not found'
    fi

    rm bin/qt.conf
    patchelf --set-rpath /usr/lib/$_pkgname bin/wemeetapp
    popd

    pushd opt/$_pkgname/bin
    rm Qt*
    find modules/ -type f -name '*.so'|xargs -I {} patchelf --set-rpath '$ORIGIN:/usr/lib/wemeet' {}
    popd
}

build() {
    cd "$srcdir"
    read -ra openssl_args < <(pkgconf --libs openssl)
    read -ra libpulse_args < <(pkgconf --cflags --libs libpulse)
    # Comment out `-D WRAP_FORCE_SINK_HARDWARE` to disable the patch that forces wemeet detects sink as hardware sink
    "${CC:-cc}" $CFLAGS -Wall -Wextra -fPIC -shared "${openssl_args[@]}" "${libpulse_args[@]}" -o libwemeetwrap.so wrap.c -D WRAP_FORCE_SINK_HARDWARE
}

package() {
    cd "$srcdir"
    cp -r usr "$pkgdir"
    cd opt/$_pkgname

    install -Dm755 "$srcdir/$_pkgname.sh" "$pkgdir/usr/bin/$_pkgname"
    ln -s "/usr/bin/$_pkgname" "$pkgdir/usr/bin/$_pkgname-x11"
    install -Dm644 $_pkgname.svg -t "$pkgdir/usr/share/icons/hicolor/scalable/apps"

    # libbugly is not likely to be necessary
    install -Dm755 lib/lib{desktop_common,ImSDK,nxui*,qt_*,service*,tms_*,ui*,wemeet*,xcast*,xnn*}.so \
        -t "$pkgdir/usr/lib/$_pkgname"
    if [ -f 'lib/libcrbase.so' ]; then
        install -Dm755 lib/libcrbase.so -t "$pkgdir/usr/lib/$_pkgname"
    else
        echo 'lib/libcrbase.so not found'
    fi

    for lib in "$pkgdir/usr/lib/$_pkgname"/*; do
        patchelf --set-rpath '$ORIGIN' "$lib"
    done

    install -dm755 "$pkgdir/opt/$_pkgname"
    cp -r bin "$pkgdir/opt/$_pkgname"
    ln -s raw/xcast.conf "$pkgdir/opt/$_pkgname/bin/xcast.conf"
    install -Dm755 "$srcdir/libwemeetwrap.so" -t "$pkgdir/usr/lib/$_pkgname"
}
