# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=eigenmodel
_pkgver=1.11
pkgname=r-${_pkgname,,}
pkgver=1.11
pkgrel=5
pkgdesc='Semiparametric Factor and Regression Models for Symmetric Relational Data'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('8dac650db4331c427c1afbfc7296889d3eb164c0b5feee99e9c37533ce0776d0')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
