# Maintainer: Anderson Rocha <anderson2320@gmail.com>

pkgname=cef-minimal
pkgver=87.1.6
_pkgcommit="g315d248"
_chromiumver="87.0.4280.66"
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

sha1sums_i686=('d7848dbbc8f0a3d40017ec62e6a046741f9ce467')
sha1sums_x86_64=('90b16aab9647df340f8cfaa46c039dbd55d9e1e5')

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
}
