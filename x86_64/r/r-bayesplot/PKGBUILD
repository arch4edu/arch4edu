# system requirements: pandoc (>= 1.12.3), pandoc-citeproc
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=bayesplot
_pkgver=1.13.0
pkgname=r-${_pkgname,,}
pkgver=1.13.0
pkgrel=1
pkgdesc='Plotting for Bayesian Models'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-dplyr
  r-ggplot2
  r-ggridges
  r-glue
  r-posterior
  r-reshape2
  r-rlang
  r-tibble
  r-tidyselect
  r-tidyr
  pandoc
)
optdepends=(
  r-ggfortify
  r-gridextra
  r-hexbin
  r-knitr
  r-loo
  r-rcolorbrewer
  r-rmarkdown
  r-rstan
  r-rstanarm
  r-rstantools
  r-scales
  r-shinystan
  r-survival
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('bdeba8c1cfdf6737a5fddb3932b854323bcae82582e370278d57ef9266de50f7')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
