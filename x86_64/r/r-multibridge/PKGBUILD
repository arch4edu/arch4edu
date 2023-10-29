# system requirements: GNU make, mpfr (>= 3.0.0), gmp (>= 6.2.1_1)
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=multibridge
_pkgver=1.2.0
pkgname=r-${_pkgname,,}
pkgver=1.2.0
pkgrel=1
pkgdesc='Evaluating Multinomial Order Restrictions with Bridge Sampling'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  mpfr
  r
  r-brobdingnag
  r-coda
  r-magrittr
  r-mvtnorm
  r-progress
  r-purrr
  r-rcpp
  r-rdpack
  r-stringr
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('6d334cfa81bef12aedaa8a12c606c38c202aa8d8ecdcb735bea03de8464c742a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
