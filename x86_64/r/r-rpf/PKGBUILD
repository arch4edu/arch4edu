# system requirements: GNU make
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=rpf
_pkgver=1.0.15
pkgname=r-${_pkgname,,}
pkgver=1.0.15
pkgrel=1
pkgdesc='Response Probability Functions'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-lifecycle
  r-mvtnorm
  r-rcpp
  r-rcppeigen
)
optdepends=(
  r-ggplot2
  r-gridextra
  r-knitr
  r-markdown
  r-mirt
  r-numderiv
  r-reshape2
  r-roxygen2
  r-testthat
)
makedepends=('make')
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('5fc12eabfe0025dfe99eee1b694a5d4a25f6e70109d7cd3c40ba421a7efbbcde')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
