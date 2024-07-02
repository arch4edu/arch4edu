# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=Cubist
_pkgver=0.4.4
pkgname=r-${_pkgname,,}
pkgver=0.4.4
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
sha256sums=('51d5fff104b69de75e08a3e14eaf67ff13ffda5be4b60f79236793475c241590')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
