# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=websocket
_pkgver=1.4.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=6
pkgdesc="'WebSocket' Client Library"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  openssl
  r-later
  r-r6
)
makedepends=(
  r-asioheaders
  r-cpp11
  websocketpp
)
optdepends=(
  r-httpuv
  r-knitr
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4e9a99ca5f1d29209393c3569b1efaa4')
b2sums=('106e13668eb329774e1829aa11a60fe4b7e405a41c5be99cbee3fea0e29d65e13c4dab3b7e1b42641aa25e0994d3ae0b26e7860a7da7d2779a7297f9caf626c5')

prepare() {
  cd "$_pkgname/src"
  # Use system websocketpp
  sed -i 's|PKG_CPPFLAGS = -I./lib|PKG_CPPFLAGS =|' Makevars.in
  sed -i 's/ws_websocketpp/websocketpp/g' websocket_defs.h websocket.cpp websocket_connection.cpp websocket_connection.h client.hpp
}

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
