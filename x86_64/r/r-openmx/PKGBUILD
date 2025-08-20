# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=OpenMx
_pkgver=2.22.9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Extended Structural Equation Modelling"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('Apache-2.0')
depends=(
  onetbb
  r-digest
  r-lifecycle
  r-rcpp
  r-rcppparallel
)
makedepends=(
  gcc-fortran
  r-bh
  r-rcppeigen
  r-rpf
  r-stanheaders
)
checkdepends=(
  r-numderiv
  r-testthat
)
optdepends=(
  r-covr
  r-ggplot2
  r-ifatools
  r-knitr
  r-lme4
  r-markdown
  r-mvtnorm
  r-numderiv
  r-reshape2
  r-rmarkdown
  r-roxygen2
  r-rpf
  r-snowfall
  r-testthat
  r-umx
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('04a3b2a1912ee4317b44d26c43846e9b')
b2sums=('912964bb43a5fd83581aa818eade3aaa9b58a5e1f91298d2e430830ddb5cec047a61aa4a28d8953e462374060c5d8e08bb95377a3f24c9201580b7c2e5eba8ac')

build() {
  mkdir build
  # compilation needs a lot of memory
  MAKEFLAGS+=" -j1"
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
