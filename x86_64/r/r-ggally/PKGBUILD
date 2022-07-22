# system requirements: openssl
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=GGally
_pkgver=2.1.2
pkgname=r-${_pkgname,,}
pkgver=2.1.2
pkgrel=4
pkgdesc="Extension to 'ggplot2'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-dplyr
  r-forcats
  r-ggplot2
  r-gtable
  r-lifecycle
  r-plyr
  r-progress
  r-rcolorbrewer
  r-reshape
  r-rlang
  r-scales
  r-tidyr
  openssl
)
optdepends=(
  r-broom
  r-broom.helpers
  r-chemometrics
  r-crosstalk
  r-emmeans
  r-geosphere
  r-ggforce
  r-hmisc
  r-igraph
  r-intergraph
  r-knitr
  r-labelled
  r-mapproj
  r-maps
  r-network
  r-nnet
  r-rmarkdown
  r-roxygen2
  r-scagnostics
  r-sna
  r-spelling
  r-survival
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('30352f36bf061bc98bdd5fa373ea0f23d007040bd908c7c018c8e627e0fb28e5')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
