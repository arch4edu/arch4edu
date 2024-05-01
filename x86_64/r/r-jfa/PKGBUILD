# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=jfa
_pkgver=0.7.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "$_pkgname-fix-tests.patch::https://github.com/koenderks/jfa/commit/6f515a5adc01ab7534a4f2b24005f5d71ea36c2b.patch")
md5sums=('2d99aa11cb75b26c85f0fde696ee2fcc'
         '854be57f42f4583c46f1c0960ee92970')
b2sums=('44d5b877d4a37394870fc6ab62ae755a87e9221a2c32ac55d7d96dc48c99c186dca94c0cf7606f4c94ddd69cf8097bae788cd3590806ff45c91e2ae2718cbd27'
        '44b992f5937df02da5ea92ae5573922a286e20364d1d3a2729bfe0876ce70853aca8d69fef234f1c7405c5b891541363289792599a308c4471513d58af8d42d8')

prepare() {
  # fix tests
  patch -Np1 -d "$_pkgname" < "$_pkgname-fix-tests.patch"
}

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
