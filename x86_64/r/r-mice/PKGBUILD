# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=mice
_pkgver=3.16.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Multivariate Imputation by Chained Equations"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
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
sha256sums=('29f0285185a540337e9dde2357690c82d174f115be701ee2f0a7083173a44040')

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
