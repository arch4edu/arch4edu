# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=bridgesampling
_pkgver=1.2-1
pkgname=r-${_pkgname,,}
pkgver=1.2.1
pkgrel=1
pkgdesc='Bridge Sampling for Marginal Likelihoods and Bayes Factors'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-brobdingnag
  r-coda
  r-mvtnorm
  r-scales
  r-stringr
)
optdepends=(
  r-bayesfactor
  r-knitr
  r-mcmcpack
  r-nimble
  r-r.rsp
  r-r2jags
  r-rcpp
  r-rcppeigen
  r-rjags
  r-rmarkdown
  r-rstan
  r-rstanarm
  r-runjags
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('e85f4fa1d1c226e485b5ffb71b83c6d80d7d6a1083795af3e526b9c87929e998')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
