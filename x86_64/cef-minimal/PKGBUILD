# Maintainer: Anderson Rocha <anderson2320@gmail.com>
# Contributor: NexAdn <nexadn@yandex.com>

pkgname=cef-minimal
pkgver="110.0.27"
_pkgcommit="g1296c82"
_chromiumver="110.0.5481.100"
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

sha1sums_i686=("254e40a3da38d50ae5c44539bac6627c9bc85bf4")
sha1sums_x86_64=("ed90e703892be39c3201e46a84faceef21825088")

[[ "$CARCH" = "i686" ]] && _arch="32"
[[ "$CARCH" = "x86_64" ]] && _arch="64"

build() {
  cd "$srcdir"/cef_binary_${_pkgver}_linux${_arch}_minimal
  sed -i 's/-Werror/#-Werror/g' cmake/cef_variables.cmake

  CMAKE_BUILD_TYPE=Release cmake .
  CMAKE_BUILD_TYPE=Release make libcef_dll_wrapper
}

package() {
  mkdir -p "$pkgdir"/opt/cef/
  cp -R "$srcdir"/cef_binary_${_pkgver}_linux${_arch}_minimal/* "$pkgdir"/opt/cef
  install -Dm644 "$srcdir"/cef_binary_${_pkgver}_linux${_arch}_minimal/LICENSE.txt "$pkgdir"/usr/share/licenses/${pkgname}/LICENSE

  # Fix read permissions
  chmod 644 "$pkgdir"/opt/cef/libcef_dll_wrapper/libcef_dll_wrapper.a
}
