# system requirements: GNU make
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=OpenMx
_pkgver=2.21.11
pkgname=r-${_pkgname,,}
pkgver=2.21.11
pkgrel=1
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
sha256sums=('152570b9cdb2d6b91f309b352458ed1b29ae2f7ce1f97c091f84c617a14071cc')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
