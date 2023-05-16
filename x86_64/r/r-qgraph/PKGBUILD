# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=qgraph
_pkgver=1.9.5
pkgname=r-${_pkgname,,}
pkgver=1.9.5
pkgrel=1
pkgdesc='Graph Plotting Methods, Psychometric Data Visualization and Graphical Model Estimation'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-abind
  r-colorspace
  r-corpcor
  r-fdrtool
  r-ggplot2
  r-glasso
  r-gtools
  r-hmisc
  r-igraph
  r-jpeg
  r-lavaan
  r-pbapply
  r-plyr
  r-png
  r-psych
  r-rcpp
  r-reshape2
)
optdepends=(
  r-bdgraph
  r-huge
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('4c5a2c7247b48d896ac56df99a07647c3f428732e1ac57b920eb0fd4e54a21d6')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
