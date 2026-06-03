# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=jfa
_pkgver=0.7.4
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
md5sums=('3c9a05b1bdc1a0d04927d147713ac711')
b2sums=('4ed07183b2e8be85f718e691c0eabdca22c939303cf640be2bbc7d5911a1f2a498dbdf2341553bdc9303566918aab0aef5968900e2fda8db50f79ff24e056e4a')

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
