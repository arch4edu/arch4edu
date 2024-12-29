# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=mice
_pkgver=3.17.0
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
md5sums=('240d70772d09ee62371d7a2ca57588f5')
b2sums=('02cd3b233e0b5eedfcb0beae2b25fc8cec5af55c6cc07b375cc05a1d7881759346944118d2a34ccafc52badd55d91f74e273d7a0b57037712b9b79234df1f9e1')

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
