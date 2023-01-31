# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=matrixcalc
_pkgver=1.0-6
pkgname=r-${_pkgname,,}
pkgver=1.0.6
pkgrel=1
pkgdesc='Collection of Functions for Matrix Calculations'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('0bc7d2f11f62d8b1969474defe27c924a243ccba0c856d585f317f6caa07f326')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
