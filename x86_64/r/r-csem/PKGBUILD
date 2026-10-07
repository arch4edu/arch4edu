# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=cSEM
_pkgver=0.7.1
pkgname=r-${_pkgname,,}
pkgver=0.7.1
pkgrel=1
pkgdesc='Composite-Based Structural Equation Modeling'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-alabama
  r-cli
  r-crayon
  r-expm
  r-future
  r-future.apply
  r-lavaan
  r-lifecycle
  r-magrittr
  r-matrixcalc
  r-matrixstats
  r-polycor
  r-progressr
  r-psych
  r-purrr
  r-rdpack
  r-rlang
  r-symmoments
  r-truncatednormal
)
optdepends=(
  r-dplyr
  r-ggplot2
  r-graphics
  r-knitr
  r-listviewer
  r-nnls
  r-openxlsx
  r-plotly
  r-prettydoc
  r-rmarkdown
  r-rootsolve
  r-testthat
  r-tidyr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('cb1faae049a7601b2f9ef3b360085dd53fe60c304b885edf55eb7448d5577733')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
