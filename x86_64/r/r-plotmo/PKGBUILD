# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=plotmo
_pkgver=3.7.1
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
md5sums=('26f6079e76c4175b8e3a89629107a85c')
b2sums=('9f2e5fe6f1ef30d930d1fe6d7d1f40fe1ab4940ac8f7a9585c6b24f69292463f7599377c8642a8513e7c02022f21b73ee41961d37d4346376108219e491e52fb')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
