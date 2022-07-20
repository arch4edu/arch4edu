# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=BoomSpikeSlab
_pkgver=1.2.5
pkgname=r-${_pkgname,,}
pkgver=1.2.5
pkgrel=1
pkgdesc='MCMC for Spike and Slab Regression'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('LGPL')
depends=(
  r
  r-boom
)
optdepends=(
  r-igraph
  r-mass
  r-mlbench
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('bc88ad95075b91799476e9e56281e4bf421106601acdbee5de783c9048b22bf8')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
