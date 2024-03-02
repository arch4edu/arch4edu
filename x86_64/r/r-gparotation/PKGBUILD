# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=GPArotation
_pkgver=2024.3-1
pkgname=r-${_pkgname,,}
pkgver=2024.3.1
pkgrel=1
pkgdesc='GPA Factor Rotation'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('88f657af29789591d581e0c529fd50ef1307abfb33e0403209bd3e591e2654da')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
