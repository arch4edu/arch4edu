# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=mice
_pkgver=3.19.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Multivariate Imputation by Chained Equations"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-broom
  r-dplyr
  r-glmnet
  r-mitml
  r-rcpp
  r-tidyr
)
makedepends=(
  r-cpp11
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-broom.mixed
  r-furrr
  r-future
  r-haven
  r-knitr
  r-literanger
  r-lme4
  r-miceadds
  r-pan
  r-parallelly
  r-purrr
  r-randomforest
  r-ranger
  r-rmarkdown
  r-rstan
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('644ce5b607f5040154453b57df584372')
b2sums=('f12e2b6121f8aa3b046cb46d82c6708a3383a3c794b0c5b149ae06643080068abd3458b3d60ae1e8354a8b5fc9feedaa1a893c97d7cf2a09b4a1f2c92258401b')

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
