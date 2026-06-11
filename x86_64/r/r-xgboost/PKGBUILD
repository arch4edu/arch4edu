# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=xgboost
_pkgver=3.2.1.1
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
  r-diagrammer
  r-diagrammersvg
  r-float
  r-ggplot2
  r-htmlwidgets
  r-igraph
  r-knitr
  r-rhpcblasctl
  r-rmarkdown
  r-rsvg
  r-testthat
  r-titanic
  r-vcd
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a7b53d16b6f255e8d3f626820937fa72')
b2sums=('0b44c854e1502201b2460ec871bd6869cd8bfbab6817de0ecfb3cc3b39f818e99c592b51d7a0668146cac7af9f50f274c562c4bfcba02d6f94d79e34d73450b9')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
