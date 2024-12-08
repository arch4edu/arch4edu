# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=DBItest
_pkgver=1.8.2
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
md5sums=('6420d02b91f87dbb5e668ffba011488f')
b2sums=('b47c83a6291bd2d2ce0db5edf420cbc7ee1e0041d0ebc582b92911775d41f8612fa9868b3b2a23fcf417180e98a465f22c2920b58a30667e0d5f715b3667d422')

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
