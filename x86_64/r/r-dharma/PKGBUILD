# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=DHARMa
_pkgver=0.4.7
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
  r-glmmadaptive
  r-glmmtmb
  r-knitr
  r-mgcviz
  r-rmarkdown
  r-sfsmisc
  r-spamm
  r-testthat
  r-phylolm
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4b8ee08f66c220e1e1ad74c6f486e747')
b2sums=('c5693a839b046f231f99ae2db6f7e46deda4120f64f0115fd044b9ede6c735472fe29c152529f9b5daf0f66935c39f5a9b31b12afd9d1a439f3968de2b16cdd2')

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
