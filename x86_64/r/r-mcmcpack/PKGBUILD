# system requirements: gcc (>= 4.0)
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=MCMCpack
_pkgver=1.7-1
pkgname=r-${_pkgname,,}
pkgver=1.7.1
pkgrel=1
pkgdesc='Markov Chain Monte Carlo (MCMC) Package'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  gcc
  r
  r-coda
  r-mcmc
  r-quantreg
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('3b0b46746324197c38826cde06729f031311c3520d9d42815b7b356d29b58529')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
