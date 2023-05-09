# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=httpuv
_cranver=1.6.10
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
sha256sums=('cd290fa9565a8a791d1ed4f4f08f0060e9fb5250bba9512646e7fd57224febf0')

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
