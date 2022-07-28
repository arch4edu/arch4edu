# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=mgm
_pkgver=1.2-13
pkgname=r-${_pkgname,,}
pkgver=1.2.13
pkgrel=1
pkgdesc='Estimating Time-Varying k-Order Mixed Graphical Models'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-glmnet
  r-gtools
  r-hmisc
  r-qgraph
  r-stringr
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('6c5581116729bb5445ce4a01c78651e3813411b869f1d07dd6075eb6a2f37951')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
