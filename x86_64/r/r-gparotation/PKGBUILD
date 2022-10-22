# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=GPArotation
_pkgver=2022.10-2
pkgname=r-${_pkgname,,}
pkgver=2022.10.2
pkgrel=1
pkgdesc='GPA Factor Rotation'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('04f72d8f3a9c204df5df904be563ec272a8437a707daee8823b2a690dde21917')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
