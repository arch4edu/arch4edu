# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=BayesFactor
_pkgver=0.9.12-4.7
pkgname=r-${_pkgname,,}
pkgver=0.9.12.4.7
pkgrel=1
pkgdesc='Computation of Bayes Factors for Common Designs'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-coda
  r-hypergeo
  r-matrixmodels
  r-mvtnorm
  r-pbapply
  r-rcpp
  r-rcppeigen
  r-stringr
)
optdepends=(
  r-arm
  r-domc
  r-foreach
  r-knitr
  r-languager
  r-lme4
  r-markdown
  r-rmarkdown
  r-testthat
  r-xtable
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('f92720697f8dbda248c7977873d582dc802522851647d563c5bcb1cada4e377d')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
