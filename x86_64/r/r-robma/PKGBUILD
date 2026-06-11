# system requirements: JAGS >= 4.3.0 (https://mcmc-jags.sourceforge.io/)
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=RoBMA
_pkgver=4.0.0
pkgname=r-${_pkgname,,}
pkgver=4.0.0
pkgrel=1
pkgdesc='Robust Bayesian Meta-Analyses'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  jags
  r
  r-bayestools
  r-ggplot2
  r-loo
  r-mvtnorm
  r-rdpack
  r-rjags
  r-rlang
  r-runjags
  r-scales
  r-loo
)
optdepends=(
  r-covr
  r-fixest
  r-knitr
  r-lme4
  r-metabma
  r-metadat
  r-metafor
  r-parallel
  r-rmarkdown
  r-testthat
  r-vdiffr
  r-weightr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('9fc78da8b60c0b8f86e14fd9529dabe3c4e1ba974e9c9e9d3ca622a3fa4763ce')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
