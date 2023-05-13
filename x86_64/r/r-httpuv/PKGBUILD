# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=httpuv
_cranver=1.6.11
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="HTTP and WebSocket Server Library"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL)
depends=(
    libuv
    r-rcpp
    r-r6
    r-promises
    r-later
    zlib
)
checkdepends=(r-curl r-testthat r-websocket)
optdepends=(
    r-testthat
    r-callr
    r-curl
    r-websocket
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('8ba79e0a8351274daf2dc566c71f88e891127cdedca62ad77a4b27a8103eeef5')

prepare() {
  # build against system libuv
  sed -i -e 's|PKG_LIBS = ./libuv/.libs/libuv.a|PKG_LIBS = -luv|' \
      -e 's|-Ilibuv/include ||' \
      -e 's|$(SHLIB): libuv/.libs/libuv.a|$(SHLIB):|' \
      "$_cranname/src/Makevars"
}

build() {
  mkdir -p build
  R CMD INSTALL "$_cranname" -l build
}

check() {
  cd "$_cranname/tests"
  R_LIBS="$srcdir/build" LC_TIME=C NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_cranname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_cranname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
