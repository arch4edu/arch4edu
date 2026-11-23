# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=caret
_pkgver=7.1-0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Classification and Regression Training"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-cli
  r-e1071
  r-foreach
  r-ggplot2
  r-plyr
  r-recipes
  r-reshape2
  r-vctrs
  r-withr
  r-yardstick
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
  r-biocmanager
  r-bradleyterry2
  r-c50
  r-covr
  r-cubist
  r-dplyr
  r-earth
  r-ellipse
  r-fastica
  r-gam
  r-gbm
  r-ipred
  r-kernlab
  r-klar
  r-knitr
  r-mda
  r-mlbench
  r-pamr
  r-party
  r-pls
  r-proxy
  r-randomforest
  r-rann
  r-rmarkdown
  r-rrf
  r-spls
  r-superpc
  r-testthat
  r-themis
  r-xgboost
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('05a3dcc39f6b7b3d881dbde6f68b0ed7')
b2sums=('8b5f140de47332c65bbcf29df36033d60b6103521e1707cea498fdc040c086474026e92736010d608ad1737e2fb365b492ef8d24eef8504c06b71974736c4fee')

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
