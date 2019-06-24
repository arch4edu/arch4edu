# Maintainer: NexAdn <nexadn@yandex.com>
pkgname=cef-minimal
pkgver=75.0.11
_pkgver="75.0.11+gf50b3c2+chromium-75.0.3770.100"
_url_pkgver="75.0.11%2Bgf50b3c2%2Bchromium-75.0.3770.100"
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
sha1sums_i686=('588ea34243c1fdadca1e80c9f5949dfde4863ca5')
sha1sums_x86_64=('46c34b27d37115f3ef66e5932f30179ae5be3628')
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
