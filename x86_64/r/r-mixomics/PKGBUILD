# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=mixOmics
_pkgver=6.28.0
pkgname=r-${_pkgname,,}
pkgver=6.28.0
pkgrel=1
pkgdesc='Omics Data Integration Project'
arch=('any')
url="https://bioconductor.org/packages/${_pkgname}"
license=('GPL')
depends=(
  r
  r-biocparallel
  r-corpcor
  r-dplyr
  r-ellipse
  r-ggplot2
  r-ggrepel
  r-gridextra
  r-igraph
  r-matrixstats
  r-rarpack
  r-rcolorbrewer
  r-reshape2
  r-tidyr
)
optdepends=(
  r-biocstyle
  r-knitr
  r-rgl
  r-rmarkdown
  r-testthat
)
source=("https://bioconductor.org/packages/release/bioc/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('72f37405011a34e5a001c0feeb397488f334154a20ada9f08bde72f2a178ed0e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
