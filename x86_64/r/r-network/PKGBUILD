# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=network
_pkgver=1.17.2
pkgname=r-${_pkgname,,}
pkgver=1.17.2
pkgrel=3
pkgdesc='Classes for Relational Data'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-magrittr
  r-statnet.common
  r-tibble
)
optdepends=(
  r-covr
  r-sna
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('9588a198807c8c68da147f479ca9af5bcb4468cf91b6a90b8044d313d9fa30f7')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
