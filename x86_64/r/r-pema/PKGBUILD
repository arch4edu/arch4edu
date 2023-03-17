# system requirements: GNU make
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=pema
_pkgver=0.1.3
pkgname=r-${_pkgname,,}
pkgver=0.1.3
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
sha256sums=('7ecacecaae13d0a15e1236fc4b641a4a897b066c18e11798d2277d8374c1bf7a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
