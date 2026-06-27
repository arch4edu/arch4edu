# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=distributional
_pkgver=0.8.1
pkgname=r-${_pkgname,,}
pkgver=0.8.1
pkgrel=1
pkgdesc='Vectorised Probability Distributions'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-digest
  r-farver
  r-generics
  r-ggplot2
  r-lifecycle
  r-numderiv
  r-pillar
  r-rlang
  r-scales
  r-vctrs
)
optdepends=(
  r-actuar
  r-covr
  r-ggdist
  r-mvtnorm
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('99c3ebb5f9e9a1a65e292326f0a7d38cd2934e0b3a3fe35006bfa2408a6dae78')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
