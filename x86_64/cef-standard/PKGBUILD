# Maintainer: Anderson Rocha <anderson2320@gmail.com>
# Contributor: etriguba <eugenetriguba@gmail.com>
# Contributor: NexAdn <nexadn@yandex.com>
pkgname=cef-standard
pkgver="121.3.7"
_pkgcommit="g82c7c57"
_chromiumver="121.0.6167.160"
_pkgver="${pkgver}+${_pkgcommit}+chromium-${_chromiumver}"
_url_pkgver="${pkgver}%2B${_pkgcommit}%2Bchromium-${_chromiumver}"
pkgrel=1
pkgdesc="Chromium Embedded Framework standard release"
arch=("x86_64")
url="https://bitbucket.org/chromiumembedded/cef"
license=("BSD")
depends=("nss" "alsa-lib" "at-spi2-atk" "pango" "libxrandr" "libxcursor" "libxss" "libxtst" "libxcomposite" "libglvnd" "dbus")
makedepends=("cmake" "make")
provides=("cef" "cef-minimal")
conflicts=("cef-minimal" "cef-git" "cef-minimal-3770-bin")
cdn_build_package_url="https://cef-builds.spotifycdn.com"

source=(
  "${cdn_build_package_url}/cef_binary_${_url_pkgver}_linux64.tar.bz2"
)

sha1sums=('5b8cf8b8130182c014daac5bcc6b8821e2c05801')

build() {
  cd "$srcdir"/cef_binary_${_pkgver}_linux64
  sed '/^add_subdirectory[\(]tests[\/].*/d' -i CMakeLists.txt
  sed 's/-Werror/#-Werror/g' -i cmake/cef_variables.cmake
  CMAKE_BUILD_TYPE=Release cmake .
  CMAKE_BUILD_TYPE=Release make libcef_dll_wrapper
}

package() {
  install -dm755 "$pkgdir"/opt/cef/
  cp -R "$srcdir"/cef_binary_${_pkgver}_linux64/* "$pkgdir"/opt/cef/
  install -Dm644 "$srcdir"/cef_binary_${_pkgver}_linux64/LICENSE.txt "$pkgdir"/usr/share/licenses/${pkgname}/LICENSE
}
