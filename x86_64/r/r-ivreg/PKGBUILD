# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ivreg
_pkgver=0.6-5
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
md5sums=('7841644fe32ca81c2db40c65773ccc50')
b2sums=('2186af0c5a19986b9e1e734a7155e08d9c21888a40037e279523448c9b2faa4025a0a29800701d5a08290aae226fa74f4480af9f94aeb1b57b58b043a4c953fc')

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
