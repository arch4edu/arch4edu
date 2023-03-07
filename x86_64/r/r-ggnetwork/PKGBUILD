# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggnetwork
_pkgver=0.5.12
pkgname=r-${_pkgname,,}
pkgver=0.5.12
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
sha256sums=('74368662c1a225cdefc8addf606b398f14dafeff03faac56c15aa5e14819e9cd')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
