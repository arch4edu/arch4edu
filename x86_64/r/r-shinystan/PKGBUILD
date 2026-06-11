# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=shinystan
_pkgver=2.7.0
pkgname=r-${_pkgname,,}
pkgver=2.7.0
pkgrel=1
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
sha256sums=('ca57fb4fe0fc926cd903f6a8da920273906b38258db371460064f1619d4f9eb9')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
