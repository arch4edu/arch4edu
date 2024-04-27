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
pkgrel=5
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
  r-subselect
  r-superpc
  r-testthat
  r-themis
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('5f4c1945b20e632187f5534a59a12c8c')
b2sums=('d3b4baa5d6234f9c1c71b62ef0d5d7cccd50e3e71f4ae54638bb6af67331a20ff689a857568a4e1280d68b18b50808d570b080a3564c1cc59c0bf1625a71bab1')

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
