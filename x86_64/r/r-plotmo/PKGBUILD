# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=plotmo
_pkgver=3.6.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
md5sums=('92a109886fbf544f525c22390171e30c')
b2sums=('db9b095c4f2e5eb177bb3bcf9fdcdedc2d5422dbe230d8d1e6e5b18d632c399d137c25284dc34a76160ca271cbfb1480853b91abe00343f0e0736e82a01e348b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
