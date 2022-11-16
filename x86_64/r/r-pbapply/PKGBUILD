# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=pbapply
_pkgver=1.6-0
pkgname=r-${_pkgname,,}
pkgver=1.6.0
pkgrel=1
pkgdesc="Adding Progress Bar to '*apply' Functions"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-shiny
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('e8c13e7edf2d2415242f5c66377fc9647dba705359ec34813fa9d2f1fbc37f61')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
