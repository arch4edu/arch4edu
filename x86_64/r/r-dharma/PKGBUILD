# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=DHARMa
_pkgver=0.5.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Residual Diagnostics for Hierarchical (Multi-Level / Mixed) Regression Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r-ape
  r-gap
  r-lme4
  r-lmtest
  r-qgam
)
checkdepends=(
  r-glmmadaptive
  r-glmmtmb
  r-mgcviz
  r-spamm
  r-testthat
)
optdepends=(
  r-brms
  r-glmmadaptive
  r-glmmtmb
  r-knitr
  r-mgcviz
  r-phylolm
  r-rmarkdown
  r-sfsmisc
  r-spamm
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f3513971c8c37d7079fde869af6047cf')
b2sums=('8f40340a0745aa628a4c4060473eadbbb68ebbaae409bfd07eefbc43d8364f6ccc20482d492b4cfa8c59adc5c22b5f482babf07db892ca706cb08cd85840ce6c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

#check() {
#  cd "$_pkgname/tests"
#  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
#}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
