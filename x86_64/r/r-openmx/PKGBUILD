# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=OpenMx
_pkgver=2.22.6
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
md5sums=('2ecaf87ba764429f785cc25454672fcf')
b2sums=('81e52904a9e411fc46b02b7f3de70d671cea6eb83a1c8c21a2c7db21a84de04d1b81bb16f2175d5234b35f3f8e72df13e777216fd06d8edbbeef78dba8c14b43')

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
