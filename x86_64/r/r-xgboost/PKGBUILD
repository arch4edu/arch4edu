# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=xgboost
_pkgver=1.7.11.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Extreme Gradient Boosting"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('Apache-2.0')
depends=(
  r-data.table
  r-jsonlite
)
optdepends=(
  r-ckmeans.1d.dp
  r-crayon
  r-diagrammer
  r-float
  r-ggplot2
  r-igraph
  r-knitr
  r-lintr
  r-rmarkdown
  r-testthat
  r-titanic
  r-vcd
  r-cplm
  r-e1071
  r-caret
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('fcb32ea43b53faf9625515a4f5197750')
b2sums=('a16d23bb8d16d488ed6a2d129b6e14dd09730be735d733ccfb4fbe188e1b138e5c62dcb3c8daa52f26197fd52110870a53372abcdf7bf734a83d307d9ab2c585')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
