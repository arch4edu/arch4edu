# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=DBItest
_pkgver=1.8.3
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
  r-pkgload
  r-rmarkdown
  r-rsqlite
  r-vctrs
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('2caccc00b2ce721cb0e44e160cad7747')
b2sums=('7969702bfe9283d65121cd84ac5b7a28d0e91f255e9c50fae3ee0d827e0e6dc236622d1f47dded0d8a25edf4cd9197735b1c596c27f4ac75cc746ef8e8c63b20')

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
