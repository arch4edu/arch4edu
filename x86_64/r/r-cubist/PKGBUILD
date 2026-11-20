# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=Cubist
_pkgver=1.0.0
pkgname=r-${_pkgname,,}
pkgver=1.0.0
pkgrel=1
pkgdesc='Rule- And Instance-Based Regression Modeling'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-reshape2
)
optdepends=(
  r-covr
  r-dplyr
  r-knitr
  r-mlbench
  r-modeldata
  r-rlang
  r-rmarkdown
  r-testthat
  r-tidyrules
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('ab2878a86ec633707488a092338ac11b13278192fec54dd4a4a28ceab4f2399b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
