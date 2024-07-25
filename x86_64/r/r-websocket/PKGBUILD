# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=websocket
_pkgver=1.4.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('7f94d3d96306c4afd2b812a04fec0468')
b2sums=('7e0b023cc18f7d4dcd2dfda4632b42d648d0a2fb00f73077b84d1af35639afb5567195903f78fde9ce8c3e21711f2391852a7bfacc02abfc1dfb1a54ad8c943b')

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
