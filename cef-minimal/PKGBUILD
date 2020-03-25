# Maintainer: NexAdn <nexadn@yandex.com>
pkgname=cef-minimal
pkgver=80.0.8
_pkgcommit="gf96cd1d"
_chromiumver="80.0.3987.132"
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
source_i686=(
    "http://opensource.spotify.com/cefbuilds/cef_binary_${_url_pkgver}_linux32_minimal.tar.bz2"
)
source_x86_64=(
    "http://opensource.spotify.com/cefbuilds/cef_binary_${_url_pkgver}_linux64_minimal.tar.bz2"
)
sha1sums_i686=('1036b653697c9089e41dee3e04aa83884b8c365c')
sha1sums_x86_64=('e6c323ff461d0f9beb093f94a77a1f817c8732e5')
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
