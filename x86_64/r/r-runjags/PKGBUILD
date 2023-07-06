# system requirements: JAGS >= 4.3.0 (https://mcmc-jags.sourceforge.io/)
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=runjags
_pkgver=2.2.2-1
pkgname=r-${_pkgname,,}
pkgver=2.2.2.1
pkgrel=1
pkgdesc='Interface Utilities, Model Templates, Parallel Computing Methods and Additional Distributions for MCMC Models in JAGS'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-coda
  jags
)
optdepends=(
  r-knitr
  r-markdown
  r-modeest
  r-rjags
  r-spelling
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('61f6ced8c7058be7b949c82e558d8898b16bdb64e9999b49a6e92bf564396229')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
