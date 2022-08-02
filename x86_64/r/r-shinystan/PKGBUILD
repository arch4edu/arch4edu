# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=shinystan
_pkgver=2.6.0
pkgname=r-${_pkgname,,}
pkgver=2.6.0
pkgrel=4
pkgdesc='Interactive Visual and Numerical Diagnostics and Posterior Analysis for Bayesian Models'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-bayesplot
  r-colourpicker
  r-dt
  r-dygraphs
  r-ggplot2
  r-gridextra
  r-gtools
  r-markdown
  r-reshape2
  r-rstan
  r-shiny
  r-shinyjs
  r-shinythemes
  r-threejs
  r-xtable
  r-xts
)
optdepends=(
  r-cmdstanr
  r-coda
  r-knitr
  r-posterior
  r-rmarkdown
  r-rsconnect
  r-rstanarm
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('a084856a2d66d8744f2c72e3e19ca35e600a508ed7ef1f7ebed8c7fc0738d529')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
