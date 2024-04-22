# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=flexsurv
_pkgver=2.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Flexible Parametric Survival and Multi-State Models"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-assertthat
  r-desolve
  r-dplyr
  r-generics
  r-ggplot2
  r-magrittr
  r-mstate
  r-muhaz
  r-mvtnorm
  r-numderiv
  r-purrr
  r-quadprog
  r-rcpp
  r-rlang
  r-rstpm2
  r-statmod
  r-tibble
  r-tidyr
  r-tidyselect
)
checkdepends=(
  r-broom
  r-covr
  r-splines2
  r-testthat
)
optdepends=(
  r-broom
  r-colorspace
  r-covr
  r-eha
  r-flexsurvcure
  r-knitr
  r-lubridate
  r-msm
  r-rmarkdown
  r-splines2
  r-survminer
  r-testthat
  r-th.data
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('3c075b4b560da1f6092d0311f44ad3c6')
b2sums=('adee84ffe15d37bdbd6aeb7099f827711c6faa3832d387eff99355a27c99f49ef99824f22a7033883624bb974a74a7aafca61ca8704d79943b396d5353733a7d')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla test_base.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
