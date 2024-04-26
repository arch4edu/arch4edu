# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=mice
_pkgver=3.16.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Multivariate Imputation by Chained Equations"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-broom
  r-dplyr
  r-generics
  r-glmnet
  r-mitml
  r-rcpp
  r-rlang
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
md5sums=('0e44a4e8e2f690d7393e90568b5b6e08')
b2sums=('e4083abf5adcedb3a096a8df0cc870852653f492aaa67eb4b2c50e17ece067f1e0bcd132e2d50aed8a959d6c4d1c192b973ffc585b8e60283e456e35efa8eed0')

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
