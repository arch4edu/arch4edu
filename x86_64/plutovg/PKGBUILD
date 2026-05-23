# Maintainer: aur.chaotic.cx

_pkgname="plutovg"
pkgname="$_pkgname"
pkgver=1.3.3
pkgrel=1
pkgdesc="Tiny 2D vector graphics library in C"
url="https://github.com/sammycage/plutovg"
license=("MIT")
arch=('x86_64')

depends=(
  'glibc'
)
makedepends=(
  'cmake'
  'git'
  'ninja'
)

provides=('libplutovg.so')

_pkgsrc="$_pkgname"
source=("$_pkgsrc"::"git+$url.git#tag=v$pkgver")
sha256sums=('03b09bab72cea11e56814b0821e7e046934d72ee224c10c91653fde8fb4aae31')

build() {
  local _cmake_options=(
    -B build
    -S "$_pkgsrc"
    -G Ninja
    -DCMAKE_BUILD_TYPE=None
    -DCMAKE_INSTALL_PREFIX='/usr'
    -DBUILD_SHARED_LIBS=ON
    -Wno-dev
  )

  cmake "${_cmake_options[@]}"
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
  install -Dm644 "$_pkgsrc/LICENSE" -t "$pkgdir/usr/share/licenses/$pkgname/"
}
