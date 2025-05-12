# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=pema
_pkgver=0.1.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Penalized Meta-Analysis"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  onetbb
  r-ggplot2
  r-rcpp
  r-rcppparallel
  r-rstan
  r-rstantools
  r-shiny
  r-sn
  r-cli
)
makedepends=(
  r-bh
  r-rcppeigen
  r-stanheaders
)
checkdepends=(
  r-mice
  r-testthat
)
optdepends=(
  r-knitr
  r-mice
  r-rmarkdown
  r-testthat
  r-webexercises
  r-bain
  r-metaforest
  r-metafor
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('699227662402fc34fdc7f508392db8c6')
b2sums=('252fbcce69d310de74e9f79743b8c99fc3e6cc298485dafc86486e7b11529addce65868245403424f80d2f4f6fd5a5b5a4dbefae55a5c03911c27e1625baf798')

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
