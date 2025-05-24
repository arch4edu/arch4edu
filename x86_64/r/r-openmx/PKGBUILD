# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=OpenMx
_pkgver=2.22.7
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
md5sums=('7e2a588ce808de11662605b06e49c63b')
b2sums=('fd04fd8b2d00ae909d837890736a2abab3cbb363f3f9bb8ef6fd5b3ecdaead6a38f6458a6ddc417f8197f4ba46a3d1dac8bfffe73405bbd9fec51be1ff1723da')

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
