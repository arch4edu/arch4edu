# system requirements: JAGS >= 4.3.0 (https://mcmc-jags.sourceforge.io/)
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=RoBMA
_pkgver=3.0.0
pkgname=r-${_pkgname,,}
pkgver=3.0.0
pkgrel=1
pkgdesc='Robust Bayesian Meta-Analyses'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  jags
  r
  r-bayestools
  r-coda
  r-ggplot2
  r-mvtnorm
  r-rdpack
  r-rjags
  r-rlang
  r-runjags
  r-scales
)
optdepends=(
  r-covr
  r-knitr
  r-metabma
  r-parallel
  r-rmarkdown
  r-rstan
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('c6092337f58f36c27b815e7e935eaab540cf884a583b3076233634524f528c9b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
