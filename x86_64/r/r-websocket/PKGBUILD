# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=websocket
_pkgver=1.4.4
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
md5sums=('67af44a6edb909e3a8ad8a371be185d0')
b2sums=('295a1f3326a2061e6ab05c2aa9aebe78cc95ccfd412eec463e3e0e99e7582a25c4011a45774dc074b2e51ddc08bc31371861de13274fa1805a8d56a4963f0d46')

prepare() {
  cd "$_pkgname/src"
  # Use system websocketpp
  sed -i 's|PKG_CPPFLAGS = -I./lib|PKG_CPPFLAGS =|' Makevars.in
  sed -i 's/ws_websocketpp/websocketpp/g' websocket_defs.h websocket.cpp websocket_connection.cpp websocket_connection.h client.hpp
  sed -i 's|io_service|io_context|' client.hpp
}

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
