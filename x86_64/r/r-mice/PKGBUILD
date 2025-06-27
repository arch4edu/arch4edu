# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=mice
_pkgver=3.18.0
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
md5sums=('c0e4bea94ab7273d9ac6af01ffe6e25d')
b2sums=('d79ee8fb9831e6a1b181faaf8c16f472552039ab05e21c251d141b383e6d5faa187fad60cd3501f494b068b65c1d70bb927b57690afbecb8b24bba439fdb31ac')

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
