# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=OpenMx
_pkgver=2.22.10
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
md5sums=('f7c4d85e242772d63cfeca8b5d462fed')
b2sums=('e3cca02fca62a9b19e283bcf86689aec293df145990126e72a8490a9a8b56aef1a5eddd40ab22df64812c5177eda12c842fd0035d62ae3db539ce1ccc69692d7')

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
