# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=flexsurv
_pkgver=2.2.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Flexible Parametric Survival and Multi-State Models"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
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
  r-testthat
)
optdepends=(
  r-colorspace
  r-eha
  r-flexsurvcure
  r-knitr
  r-lubridate
  r-msm
  r-rmarkdown
  r-survminer
  r-testthat
  r-th.data
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a86c5647062c60b2bebb5ffb8165604f')
sha256sums=('6635750e40c5ffd5648fa3539208ca0c761953a724ef110225fd625762d450e3')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla test_base.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
