# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=AER
_pkgver=1.2-15
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
md5sums=('7c4fea52fd24319c6566533f01ae1e88')
b2sums=('156d0b7ed49c458a593f5b72999dc7e8f078f4c1c7aa5ee1414bf9b55b1972ce69745edb16fa86c557104286acc0ba85e4045e7ba31950a1bf195535ea8617a9')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
