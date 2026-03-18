# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=fixest
_pkgver=0.14.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Fast Fixed-Effects Estimations"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-dreamerr
  r-numderiv
  r-rcpp
  r-sandwich
  r-stringmagic
)
checkdepends=(
  r-data.table
)
optdepends=(
  r-aer
  r-data.table
  r-emmeans
  r-estimability
  r-ggplot2
  r-knitr
  r-lfe
  r-pander
  r-pdftools
  r-plm
  r-rmarkdown
  r-tinytex
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1b060230d38e4ec6df385a6be0ea1d6a')
b2sums=('6e0607c0d43a3e3a5003850f651d82143823c47c1f94c39fa54d035cfbfa6f8661bb8859c5da13c3fdda34e7b7f46a19ec073a5a22403f70377cb7b79b905038')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" Rscript --vanilla fixest_tests.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
