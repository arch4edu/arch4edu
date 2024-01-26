# system requirements: GNU make, C++14
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=xgboost
_pkgver=1.7.7.1
pkgname=r-${_pkgname,,}
pkgver=1.7.7.1
pkgrel=1
pkgdesc='Extreme Gradient Boosting'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('Apache')
depends=(
  r
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
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('f7912ccf3a583a27208f74ca15c3b272cc930bae6b10ae7e5958ff2951ee9723')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
