# system requirements: pandoc (>= 1.12.3)
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=bayesplot
_pkgver=1.16.0
pkgname=r-${_pkgname,,}
pkgver=1.16.0
pkgrel=2
pkgdesc='Plotting for Bayesian Models'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL-3.0-or-later')
depends=(
  r-dplyr
  r-ggdist
  r-ggplot2
  r-ggridges
  r-glue
  r-lifecycle
  r-posterior
  r-reshape2
  r-rlang
  r-tibble
  r-tidyselect
  r-tidyr
  pandoc
)
optdepends=(
  r-cmdstanr
  r-ggfortify
  r-gridextra
  r-hexbin
  r-knitr
  r-loo
  r-monotone
  r-patchwork
  r-rcolorbrewer
  r-rmarkdown
  r-rstan
  r-rstanarm
  r-rstantools
  r-scales
  r-shinystan
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('1602f1232ddc83c386e9964ac54eb9a10d51f562093b658836933aa6b6481aeb')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
