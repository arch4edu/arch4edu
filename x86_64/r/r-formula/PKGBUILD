# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=Formula
_pkgver=1.2-4
pkgname=r-${_pkgname,,}
pkgver=1.2.4
pkgrel=4
pkgdesc='Extended Model Formulas'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('cb70e373b5ed2fc8450937fb3321d37dfd22dcc6f07cb872a419d51205125caf')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
