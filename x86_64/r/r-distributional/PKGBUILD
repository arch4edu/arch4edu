# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=distributional
_pkgver=0.3.2
pkgname=r-${_pkgname,,}
pkgver=0.3.2
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
sha256sums=('c883d633398233aee5a8ca6b587687f765bdfe0732a84e4961e7f71ac0d008f8')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
