# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ivreg
_pkgver=0.6-7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Instrumental-Variables Regression by '2SLS', '2SM', or '2SMM', with Diagnostics"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-car
  r-formula
  r-lmtest
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-aer
  r-effects
  r-ggplot2
  r-gt
  r-insight
  r-knitr
  r-modelsummary
  r-rmarkdown
  r-sandwich
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('b79da16d7ea9b34b6274f00a007db256')
b2sums=('c61fc8046b6adfd56a40a7cb94ea1db173921acf61b9f938e1b09275ab3b27d76a6038fe6e231a8284c42ee5ed008011320e9d5d467f77ca2fc57231ea3a5719')

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
