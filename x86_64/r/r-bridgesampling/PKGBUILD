# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=bridgesampling
_pkgver=1.1-2
pkgname=r-${_pkgname,,}
pkgver=1.1.2
pkgrel=4
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
sha256sums=('54ecd39aa2e36d4d521d3d36425f9fe56a3f8547df6048c814c5931d790f3e6b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
