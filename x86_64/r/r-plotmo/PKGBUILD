# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=plotmo
_pkgver=3.7.0
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
md5sums=('e3750064bbe059bf4fa12ef93aee5ca5')
b2sums=('6fb8a34511770f7f9f7371ad1c671c70da151c4338ea17aff908eb50e4e3592df14eb7bd2f6f061b302fe48db6af788b5f975b440039a4a43fd9ce9ba9757162')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
