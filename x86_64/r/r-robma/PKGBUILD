# system requirements: JAGS >= 4.3.0 (https://mcmc-jags.sourceforge.io/)
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=RoBMA
_pkgver=3.2.0
pkgname=r-${_pkgname,,}
pkgver=3.2.0
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
  r-mvtnorm
  r-rdpack
  r-rjags
  r-rlang
  r-runjags
  r-scales
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
sha256sums=('cdb27398fa9761dcd978ec10c7b3a8779cfbac007d8438750b3b20de399e4f9d')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
