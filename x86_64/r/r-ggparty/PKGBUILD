# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=ggparty
_pkgver=1.0.0.1
pkgname=r-${_pkgname,,}
pkgver=1.0.0.1
pkgrel=1
pkgdesc="'ggplot' Visualizations for the 'partykit' Package"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-checkmate
  r-ggplot2
  r-gtable
  r-partykit
  r-rlang
)
optdepends=(
  r-aer
  r-coin
  r-knitr
  r-mass
  r-mlbench
  r-pander
  r-rmarkdown
  r-testthat
  r-th.data
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('c0d1b31e0607c7698242602c22507a231a9c377d342071d774c33dbc28885c74')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
