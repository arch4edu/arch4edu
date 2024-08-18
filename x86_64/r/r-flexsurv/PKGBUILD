# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=flexsurv
_pkgver=2.3.2
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
md5sums=('b46668f4d46554e6dc90fd6a0bb54f7f')
b2sums=('637ec54e4f0fbc249c9e355b59f86782a831a4d7603aa25af8ab460fca26a82f2b2efa45ebf34e85108901f419275a698aee6c22355f20012b8565c1ad8fb7b9')

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
