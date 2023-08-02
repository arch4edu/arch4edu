# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=websocket
_pkgver=1.4.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="'WebSocket' Client Library"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL2)
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
sha256sums=('281fa0e5d8739ef90626117c8d5ca9e30c7aeb642346d16706cbca34a46749cf')

prepare() {
  cd "$_pkgname/src"
  # Use system websocketpp
  sed -i 's|PKG_CPPFLAGS = -I./lib|PKG_CPPFLAGS =|' Makevars.in
  sed -i 's/ws_websocketpp/websocketpp/g' websocket_defs.h websocket.cpp websocket_connection.cpp websocket_connection.h client.hpp
}

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
