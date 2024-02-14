# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggnetwork
_pkgver=0.5.13
pkgname=r-${_pkgname,,}
pkgver=0.5.13
pkgrel=1
pkgdesc="Geometries to Plot Networks with 'ggplot2'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-ggplot2
  r-ggrepel
  r-igraph
  r-network
  r-sna
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('6c297ead19dbd89de3278f3705410b757f2d9744bc466d8175105833a4e1fd46')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
