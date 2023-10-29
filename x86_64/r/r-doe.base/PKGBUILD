# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=DoE.base
_pkgver=1.2-3
pkgname=r-${_pkgname,,}
pkgver=1.2.3
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
sha256sums=('35b87591046ec86d0f9968dd39310eec0684ea4f37db05f9368bf1aaf38f3bd4')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
