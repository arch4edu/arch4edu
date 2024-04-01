# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=DBItest
_pkgver=1.8.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Testing DBI Backends"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('LGPL-2.1-or-later')
depends=(
  r-blob
  r-callr
  r-dbi
  r-desc
  r-hms
  r-lubridate
  r-magrittr
  r-nanoarrow
  r-palmerpenguins
  r-rlang
  r-testthat
  r-withr
)
optdepends=(
  r-clipr
  r-constructive
  r-debugme
  r-devtools
  r-knitr
  r-lintr
  r-pkgload
  r-rmarkdown
  r-rsqlite
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4c364d7e113a1ed755412a9601c4be00')
b2sums=('634b480e4a697b64b572e6957909845d279332a7fa0d8dd4c72bba81a29867dd2a798227a73623f8ed0aaedac0f69bd27cd66bafa7b1570b28c7b61ac426ff9c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
