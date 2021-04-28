# Maintainer: etriguba <eugenetriguba@gmail.com>
# Previous Maintainer: NexAdn <nexadn@yandex.com>
pkgname=cef-standard
pkgver=90.5.10
_pkgcommit="gf2f0bfb"
_chromiumver="90.0.4430.85"
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
conflicts=("cef-minimal" "cef-git" "cef-minimal-3770-bin")
source_i686=(
    "https://cef-builds.spotifycdn.com/cef_binary_${_url_pkgver}_linux32.tar.bz2"
)
source_x86_64=(
    "https://cef-builds.spotifycdn.com/cef_binary_${_url_pkgver}_linux64.tar.bz2"
)
sha1sums_i686=('78b0ba44eb6f6983ce3195c83903bc08e0cea6f0')
sha1sums_x86_64=('788f8f0dd9a9cb7b2d98cc07e8da418ab4542942')
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
