# system requirements: GNU make
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=OpenMx
_pkgver=2.20.6
pkgname=r-${_pkgname,,}
pkgver=2.20.6
pkgrel=6
pkgdesc='Extended Structural Equation Modelling'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('Apache')
depends=(
  r
  r-bh
  r-digest
  r-lifecycle
  r-rcpp
  r-rcppeigen
  r-rcppparallel
  r-rpf
  r-stanheaders
)
optdepends=(
  r-covr
  r-ggplot2
  r-ifatools
  r-knitr
  r-lme4
  r-markdown
  r-mvtnorm
  r-numderiv
  r-reshape2
  r-rmarkdown
  r-roxygen2
  r-rpf
  r-snowfall
  r-testthat
  r-umx
)
makedepends=(
  gcc-fortran
  make
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('65c50ce09f9c006b41b7311ec05eba3ae77926d84fb44e3905905208404826ed')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
