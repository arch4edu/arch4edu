# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=xgboost
_pkgver=1.7.10.1
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
md5sums=('6830eed1c87743a14e44a8aac9b13685')
b2sums=('bd36dcbe2035c71a1e103810d269399b8056d05d7f5a347cf9aaab02e17c93ce7051f327ac87aaf2523429f2a11ebf0638c77596dbe20d50da99530f69c26599')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
