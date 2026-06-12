# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=AER
_pkgver=1.2-16
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Applied Econometrics with R"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only OR GPL-3.0-only')
depends=(
  r-car
  r-formula
  r-lmtest
  r-sandwich
  r-zoo
)
optdepends=(
  r-dynlm
  r-effects
  r-fgarch
  r-forecast
  r-ineq
  r-longmemo
  r-mlogit
  r-np
  r-plm
  r-pscl
  r-quantreg
  r-rgl
  r-rocr
  r-rugarch
  r-sampleselection
  r-scatterplot3d
  r-strucchange
  r-systemfit
  r-truncreg
  r-tseries
  r-urca
  r-vars
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('88bee5867e7063c2c27d04ba09211a7f')
b2sums=('4f3d9f9ab48d3402b0fcbb533c26d8eb9425366df7ece1d675a9e5e4a33620d5d28edea1f753687b567e96a8dcb5eab58f1ed54926797f1e21601b0b00b26666')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
