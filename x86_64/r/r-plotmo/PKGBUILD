# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=plotmo
_pkgver=3.6.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Plot a Model's Residuals, Response, and Partial Dependence Plots"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-formula
  r-plotrix
)
optdepends=(
  r-c50
  r-earth
  r-gbm
  r-glmnet
  r-glmnetutils
  r-mlr
  r-neuralnet
  r-partykit
  r-pre
  r-rpart.plot
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('b81972271013a38144b292271edc312d')
b2sums=('ceaebeb3853adb45831c12023c8bf0034d931870f97102f1898fdea848b312f01b66ec4e0f4406b01bafe94ec38b50d73e2cab04e2096402278910a48796fb72')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
