# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=networktools
_pkgver=1.5.2
pkgname=r-${_pkgname,,}
pkgver=1.5.2
pkgrel=1
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
sha256sums=('877045b0560007df40a476f60cb871e05d6264bf6bd49d1e3ddb9668992d5870')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
