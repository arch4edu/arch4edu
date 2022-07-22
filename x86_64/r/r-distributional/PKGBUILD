# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=distributional
_pkgver=0.3.0
pkgname=r-${_pkgname,,}
pkgver=0.3.0
pkgrel=4
pkgdesc='Vectorised Probability Distributions'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-digest
  r-ellipsis
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
sha256sums=('fab36c7346617d8f2ca4b3cd0e3c9da93cb2f95fb7f102a3ae88670e694751d6')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
