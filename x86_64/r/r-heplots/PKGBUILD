# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=heplots
_pkgver=1.4-2
pkgname=r-${_pkgname,,}
pkgver=1.4.2
pkgrel=3
pkgdesc='Visualizing Hypothesis Tests in Multivariate Linear Models'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-broom
  r-car
  r-magrittr
  r-purrr
  r-tibble
)
optdepends=(
  r-animation
  r-bookdown
  r-candisc
  r-corrgram
  r-dplyr
  r-effects
  r-ggplot2
  r-gplots
  r-knitr
  r-lattice
  r-mvinfluence
  r-nlme
  r-reshape
  r-reshape2
  r-rgl
  r-rmarkdown
  r-tidyr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('5d48d3971939fd54c756abffb90c913933d7531ae9ba9d4eeecc8f3e043fd3ce')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
