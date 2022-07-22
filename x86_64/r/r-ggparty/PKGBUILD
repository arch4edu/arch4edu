# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=ggparty
_pkgver=1.0.0
pkgname=r-${_pkgname,,}
pkgver=1.0.0
pkgrel=4
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
sha256sums=('0e7b29ee4519306c81f5c17f08131d6c466f3ee68f4b65e41d7482916ec9d068')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
