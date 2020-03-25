# Maintainer: NexAdn <nexadn@yandex.com>
pkgname=cef-standard
pkgver=80.0.8
_pkgcommit="gf96cd1d"
_chromiumver="80.0.3987.132"
_pkgver="${pkgver}+${_pkgcommit}+chromium-${_chromiumver}"
_url_pkgver="${pkgver}%2B${_pkgcommit}%2Bchromium-${_chromiumver}"
pkgrel=1
pkgdesc="Chromium Embedded Framework standard release"
arch=("i686" "x86_64")
url="https://bitbucket.org/chromiumembedded/cef"
license=("BSD")
depends=("nss" "alsa-lib" "at-spi2-atk" "pango" "libxrandr" "libxcursor" "libxss" "libxtst" "libxcomposite" "libglvnd" "dbus")
makedepends=("cmake" "make")
provides=("cef" "cef-minimal")
conflicts=("cef-minimal" "cef-git")
source_i686=(
    "http://opensource.spotify.com/cefbuilds/cef_binary_${_url_pkgver}_linux32.tar.bz2"
)
source_x86_64=(
    "http://opensource.spotify.com/cefbuilds/cef_binary_${_url_pkgver}_linux64.tar.bz2"
)
sha1sums_i686=('9e30fa535f9200d1da34f2a742e3973db9f8c5e4')
sha1sums_x86_64=('176d0c6d017c4532dc1d79fd50a5619644b314d5')
[[ "$CARCH" = "i686" ]] && _arch="32"
[[ "$CARCH" = "x86_64" ]] && _arch="64"
build() {
    cd "$srcdir"/cef_binary_${_pkgver}_linux${_arch}
    sed '/^add_subdirectory[\(]tests[\/].*/d' -i CMakeLists.txt
    sed 's/-Werror/#-Werror/g' -i cmake/cef_variables.cmake
    cmake .
    make clean
    make libcef_dll_wrapper
}
package() {
    install -dm755 "$pkgdir"/opt/cef/
    cp -R "$srcdir"/cef_binary_${_pkgver}_linux${_arch}/* "$pkgdir"/opt/cef/
    install -Dm644 "$srcdir"/cef_binary_${_pkgver}_linux${_arch}/LICENSE.txt "$pkgdir"/usr/share/licenses/${pkgname}/LICENSE
}
