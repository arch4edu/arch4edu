# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=caret
_pkgver=7.0-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Classification and Regression Training"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
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
  r-superpc
  r-testthat
  r-themis
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('c11d2d954241566f577841a58d101f75')
b2sums=('ccc91789541348ef43578db2e88d16df482b4cc95e90f26034da007a59f4bc5987022e16440d427b402dd980b74b21c7c74f40241d9d92b1b90373241451cc37')

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
