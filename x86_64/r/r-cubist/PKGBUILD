# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=Cubist
_pkgver=0.6.0
pkgname=r-${_pkgname,,}
pkgver=0.6.0
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
sha256sums=('7a09e5f4bde4c60ea5d856ad39260a472dd696eda4d8a9b8f5a25d4fa5cfb836')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
