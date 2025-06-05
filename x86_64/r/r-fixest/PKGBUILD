# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=fixest
_pkgver=0.12.1
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
md5sums=('fb9d278858abd82781a01b2fc0ed9b8c')
b2sums=('076ad658827515c6bcca6304a84ad56801a7b54c4583ca34b502c6a0f4a747f87e0b9fc6d04bb5c9b4ee5182b0b1385f2afc35c2c35616692e8f610fc06fa75e')

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
