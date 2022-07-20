# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=Deriv
_pkgver=4.1.3
pkgname=r-${_pkgname,,}
pkgver=4.1.3
pkgrel=4
pkgdesc='Symbolic Differentiation'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('dbdbf5ed8babf706373ae33a937d013c46110a490aa821bcd158a70f761d0f8c')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
