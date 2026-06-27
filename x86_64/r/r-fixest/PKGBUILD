# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=fixest
_pkgver=0.14.2
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
md5sums=('f891b42dad8b85a7ef20ce44ecf590ee')
b2sums=('defece26d4e4414e73b9e79771dcf0bb0c0fd967c8eadcd61b71999ae596e0399a110b73e33b42f80ccafcf6a3012245f1e2c99c9f9bd0e50687545ec0ebf498')

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
