# Maintainer: Anderson Rocha <anderson2320@gmail.com>
# Contributor: etriguba <eugenetriguba@gmail.com>
# Contributor: NexAdn <nexadn@yandex.com>
pkgname=cef-standard
pkgver="111.2.6"
_pkgcommit="g491d238"
_chromiumver="111.0.5563.65"
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
cdn_build_package_url="https://cef-builds.spotifycdn.com"

source_i686=(
  "${cdn_build_package_url}/cef_binary_${_url_pkgver}_linux32.tar.bz2"
)
source_x86_64=(
  "${cdn_build_package_url}/cef_binary_${_url_pkgver}_linux64.tar.bz2"
)

sha1sums_i686=("c3311f258b37dd10bae6e2811b0b2c8aca99ca30")
sha1sums_x86_64=("5f2cf98277ae915f63f3eba3869ad3697c35183d")

[[ "$CARCH" = "i686" ]] && _arch="32"
[[ "$CARCH" = "x86_64" ]] && _arch="64"

build() {
  cd "$srcdir"/cef_binary_${_pkgver}_linux${_arch}
  sed '/^add_subdirectory[\(]tests[\/].*/d' -i CMakeLists.txt
  sed 's/-Werror/#-Werror/g' -i cmake/cef_variables.cmake
  CMAKE_BUILD_TYPE=Release cmake .
  CMAKE_BUILD_TYPE=Release make libcef_dll_wrapper
}

package() {
  install -dm755 "$pkgdir"/opt/cef/
  cp -R "$srcdir"/cef_binary_${_pkgver}_linux${_arch}/* "$pkgdir"/opt/cef/
  install -Dm644 "$srcdir"/cef_binary_${_pkgver}_linux${_arch}/LICENSE.txt "$pkgdir"/usr/share/licenses/${pkgname}/LICENSE
}
