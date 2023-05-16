# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=bootnet
_pkgver=1.5.1
pkgname=r-${_pkgname,,}
pkgver=1.5.1
pkgrel=1
pkgdesc='Bootstrap Methods for Various Network Estimation Routines'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-abind
  r-corpcor
  r-dplyr
  r-ggplot2
  r-gtools
  r-igraph
  r-isingfit
  r-isingsampler
  r-mgm
  r-mvtnorm
  r-networktoolbox
  r-networktools
  r-pbapply
  r-qgraph
  r-rlang
  r-snow
  r-tibble
  r-tidyr
)
optdepends=(
  r-bdgraph
  r-ggmncv
  r-glasso
  r-graphicalvar
  r-huge
  r-lavaan
  r-psychtools
  r-relaimpo
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('0ef10d1acf41987def70a3ee86968c7f590aa0e5d895b797b5ba8085ed197bdd')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
