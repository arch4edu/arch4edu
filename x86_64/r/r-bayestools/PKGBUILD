# system requirements: JAGS >= 4.3.0 (https://mcmc-jags.sourceforge.io/)
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=BayesTools
_pkgver=0.2.12
pkgname=r-${_pkgname,,}
pkgver=0.2.12
pkgrel=1
pkgdesc='Tools for Bayesian Analyses'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-bridgesampling
  r-coda
  r-extradistr
  r-ggplot2
  r-mvtnorm
  r-rdpack
  r-rjags
  r-runjags
  jags
)
optdepends=(
  r-bayesfactor
  r-covr
  r-knitr
  r-rmarkdown
  r-rstan
  r-scales
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('e9b979157d13787eabb40eaa0f87e8eeeafa7a789225c7ebed7c19356f39a763')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
