# system requirements: GNU make
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=pema
_pkgver=0.1.2
pkgname=r-${_pkgname,,}
pkgver=0.1.2
pkgrel=1
pkgdesc='Penalized Meta-Analysis'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-bh
  r-ggplot2
  r-rcpp
  r-rcppeigen
  r-rcppparallel
  r-rstan
  r-rstantools
  r-shiny
  r-sn
  r-stanheaders
)
optdepends=(
  r-knitr
  r-mice
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('0d3c2098dfd713cb0e6c198a8c18ce5b62fc576cae337bda8f92060a7a459c8f')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
