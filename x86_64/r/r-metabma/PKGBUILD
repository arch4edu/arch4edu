# system requirements: GNU make
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=metaBMA
_pkgver=0.6.7
pkgname=r-${_pkgname,,}
pkgver=0.6.7
pkgrel=3
pkgdesc='Bayesian Model Averaging for Random and Fixed Effects Meta-Analysis'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-bh
  r-bridgesampling
  r-coda
  r-laplacesdemon
  r-logspline
  r-mvtnorm
  r-rcpp
  r-rcppeigen
  r-rcppparallel
  r-rstan
  r-rstantools
  r-stanheaders
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-spelling
  r-testthat
)
makedepends=('make')
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('330bccb4b2297bc3a8b7291197c5e978b90b002907f762ede40f2d3e383367da')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
