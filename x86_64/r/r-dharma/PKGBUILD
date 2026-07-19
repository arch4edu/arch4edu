# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=DHARMa
_pkgver=0.5.0
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
md5sums=('526afecc23a72067743268a25f97fab2')
b2sums=('e2ead9086fa5265c1dfa7ed035d4c45c0a44b34d88e37f9d709072ff28efbdce45547a5ac29976fcf0b4e875e67125224ca5c5d88954507d79fab6ac6fe2f835')

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
