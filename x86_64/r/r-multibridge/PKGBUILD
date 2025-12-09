# system requirements: GNU make, mpfr (>= 3.0.0), gmp (>= 6.2.1_1)
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=multibridge
_pkgver=1.3.0
pkgname=r-${_pkgname,,}
pkgver=1.3.0
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
sha256sums=('ac8f779961ce702d8a226c36e97d396685ac7eb890269c3e874253ac41216d89')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
