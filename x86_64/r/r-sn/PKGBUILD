# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=sn
_pkgver=2.1.1
pkgname=r-${_pkgname,,}
pkgver=2.1.1
pkgrel=1
pkgdesc='The Skew-Normal and Related Distributions Such as the Skew-t and the SUN'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-mnormt
  r-numderiv
  r-quantreg
)
optdepends=(
  r-r.rsp
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('f9f6b56d91dc7cb18dc8308d0875b9648c90b268d1aaf8f4c5164ff016df22bd')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
