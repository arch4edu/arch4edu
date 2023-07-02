# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=httpuv
_pkgver=1.6.11
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="HTTP and WebSocket Server Library"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
depends=(
  libuv
  r-later
  r-promises
  r-r6
  r-rcpp
  zlib
)
checkdepends=(
  r-curl
  r-testthat
  r-websocket
)
optdepends=(
  r-callr
  r-curl
  r-testthat
  r-websocket
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "system-libuv.patch")
md5sums=('38ca2017f9a45faa2f45df08de147096'
         'f3a1ba807642c566ae7a47fd33fc9911')
sha256sums=('8ba79e0a8351274daf2dc566c71f88e891127cdedca62ad77a4b27a8103eeef5'
            '555ba06ceb96fe3d944ae189c07671034db6033b8bad61ce740f6cb44dbac855')

prepare() {
  # build against system libuv and link to zlib
  patch -Np1 -i system-libuv.patch
}

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" LC_TIME=C NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
