# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ellipse
_pkgver=0.4.3
pkgname=r-${_pkgname,,}
pkgver=0.4.3
pkgrel=1
pkgdesc='Functions for Drawing Ellipses and Ellipse-Like Confidence Regions'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-mass
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('02ef2b11c3462a8b800332e522183f4c7c40c7d2d66c5174d5f3f6d8cc68a946')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
