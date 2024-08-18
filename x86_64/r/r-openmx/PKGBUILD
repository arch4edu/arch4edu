# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=OpenMx
_pkgver=2.21.12
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
md5sums=('d0802ee9a9d1ecce02d0e2bd7c8a6948')
b2sums=('cef22428cd9e87882aa463b2ede368365ce637a4e54a4142659a5f23697cc947898280370d1c610593cdad09947a1f779ccfa864fb95f7f8609151cee4cfca76')

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
