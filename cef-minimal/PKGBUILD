# Maintainer: Anderson Rocha <anderson2320@gmail.com>

pkgname=cef-minimal
pkgver=88.2.8
_pkgcommit="ge484012"
_chromiumver="88.0.4324.150"
_pkgver="${pkgver}+${_pkgcommit}+chromium-${_chromiumver}"
_url_pkgver="${pkgver}%2B${_pkgcommit}%2Bchromium-${_chromiumver}"
pkgrel=1
pkgdesc="Chromium Embedded Framework minimal release"
arch=("i686" "x86_64")
url="https://bitbucket.org/chromiumembedded/cef"
license=("BSD")
depends=("nss" "alsa-lib" "libxss" "libxtst" "libglvnd" "pango" "libxcursor" "dbus" "libxrandr" "libxcomposite" "at-spi2-atk")
makedepends=("cmake" "make")
provides=("cef")
conflicts=("cef-standard" "cef-git")
cdn_build_package_url="https://cef-builds.spotifycdn.com"

source_i686=(
    "${cdn_build_package_url}/cef_binary_${_url_pkgver}_linux32_minimal.tar.bz2"
)
source_x86_64=(
    "${cdn_build_package_url}/cef_binary_${_url_pkgver}_linux64_minimal.tar.bz2"
)

sha1sums_i686=('f3dec9b8c13590a4b88c782862a9c69c5bb9c986')
sha1sums_x86_64=('0ff708f6104fab3e43fbcd41d0a9aea6f69bc3f5')

[[ "$CARCH" = "i686" ]] && _arch="32"
[[ "$CARCH" = "x86_64" ]] && _arch="64"

build() {
    cd "$srcdir"/cef_binary_${_pkgver}_linux${_arch}_minimal
    sed -i 's/-Werror/#-Werror/g' cmake/cef_variables.cmake
    cmake .
    make libcef_dll_wrapper
}

package() {
    mkdir -p "$pkgdir"/opt/cef/
    cp -R "$srcdir"/cef_binary_${_pkgver}_linux${_arch}_minimal/* "$pkgdir"/opt/cef
    install -Dm644 "$srcdir"/cef_binary_${_pkgver}_linux${_arch}_minimal/LICENSE.txt "$pkgdir"/usr/share/licenses/${pkgname}/LICENSE

    # Fix read permissions
    chmod 644 "$pkgdir"/opt/cef/libcef_dll_wrapper/libcef_dll_wrapper.a
}
