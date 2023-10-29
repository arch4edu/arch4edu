# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=caret
_pkgver=6.0-94
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Classification and Regression Training"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
depends=(
  r-e1071
  r-foreach
  r-ggplot2
  r-modelmetrics
  r-plyr
  r-proc
  r-recipes
  r-reshape2
  r-withr
)
checkdepends=(
  r-earth
  r-fastica
  r-glmnet
  r-kernlab
  r-mda
  r-mlmetrics
  r-randomforest
  r-testthat
  r-themis
)
optdepends=(
  r-bradleyterry2
  r-covr
  r-cubist
  r-dplyr
  r-earth
  r-ellipse
  r-fastica
  r-gam
  r-ipred
  r-kernlab
  r-klar
  r-knitr
  r-mda
  r-mlbench
  r-mlmetrics
  r-pamr
  r-party
  r-pls
  r-proxy
  r-randomforest
  r-rann
  r-rmarkdown
  r-spls
  r-subselect
  r-superpc
  r-testthat
  r-themis
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('5f4c1945b20e632187f5534a59a12c8c')
sha256sums=('2715e83ca260bb739cd926a55b0d2da1e3f6308b17b56862466e738d930d29a8')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
