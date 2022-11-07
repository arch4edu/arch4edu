# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=ggrepel
_pkgver=0.9.2
pkgname=r-${_pkgname,,}
pkgver=0.9.2
pkgrel=1
pkgdesc="Automatically Position Non-Overlapping Text Labels with 'ggplot2'"
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-ggplot2
  r-rcpp
  r-rlang
  r-scales
)
optdepends=(
  r-devtools
  r-dplyr
  r-ggbeeswarm
  r-gridextra
  r-knitr
  r-magrittr
  r-prettydoc
  r-readr
  r-rmarkdown
  r-stringr
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('0a3088c48177528e2a65defebbc4f09a744ebb44408588f688811f8d0d827488')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
