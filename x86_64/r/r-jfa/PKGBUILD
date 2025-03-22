# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=jfa
_pkgver=0.7.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Statistical Methods for Auditing"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  onetbb
  r-bde
  r-extradistr
  r-ggplot2
  r-rcpp
  r-rcppparallel
  r-rstan
  r-rstantools
  r-truncdist
)
makedepends=(
  r-bh
  r-rcppeigen
  r-stanheaders
)
checkdepends=(
  r-benford.analysis
  r-benfordtests
  r-beyondbenford
  r-fairness
  r-mus
  r-rmarkdown
  r-samplingbook
  r-testthat
)
optdepends=(
  r-benford.analysis
  r-benfordtests
  r-beyondbenford
  r-fairness
  r-knitr
  r-mus
  r-rmarkdown
  r-samplingbook
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('c141fd3b12d9e67dd70181abc053a7a4')
b2sums=('663bf69fdd86604580038c93c0cbde824530d5df8a55145e206e168af2058c29bd2083d14c2ad241d63f08ed2e7e26fa035a5a95a227b12c315a155180e1efcb')

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
