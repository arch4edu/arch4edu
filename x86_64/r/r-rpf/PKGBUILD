# system requirements: GNU make
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=rpf
_pkgver=1.0.14
pkgname=r-${_pkgname,,}
pkgver=1.0.14
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
sha256sums=('e4bb090a810ec4e70a23547f95e1e07ce0229e38fbbbbe22abfad98e9b33f796')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
