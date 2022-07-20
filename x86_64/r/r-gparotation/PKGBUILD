# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=GPArotation
_pkgver=2022.4-1
pkgname=r-${_pkgname,,}
pkgver=2022.4.1
pkgrel=5
pkgdesc='GPA Factor Rotation'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('231e7edcdcc091fbecfb4f2e88d1a4344967cf7ea58074b385a4b8b48d9da224')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
