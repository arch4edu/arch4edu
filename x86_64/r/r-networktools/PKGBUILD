# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=networktools
_pkgver=1.5.0
pkgname=r-${_pkgname,,}
pkgver=1.5.0
pkgrel=4
pkgdesc='Tools for Identifying Important Nodes in Networks'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-cocor
  r-eigenmodel
  r-ggplot2
  r-gridextra
  r-igraph
  r-psych
  r-qgraph
  r-r.utils
  r-rcolorbrewer
  r-reshape2
  r-smacof
  r-wordcloud
)
optdepends=(
  r-dplyr
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('1a51860d0fa4c5225b00c2a68f18a4d9d736f412102b0fe84b643e4948c11343')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
