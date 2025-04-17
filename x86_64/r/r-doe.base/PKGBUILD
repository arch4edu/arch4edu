# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=DoE.base
_pkgver=1.2-5
pkgname=r-${_pkgname,,}
pkgver=1.2.5
pkgrel=1
pkgdesc='Full Factorials, Orthogonal Arrays and Base Utilities for DoE Packages'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-combinat
  r-conf.design
  r-numbers
  r-partitions
  r-vcd
)
optdepends=(
  r-doe.wrapper
  r-frf2
  r-rcolorbrewer
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('59cc4e2afe7bef792d454655258e8f4eb073cf3fdcb9639237f83e2fe1b7f4b9')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
