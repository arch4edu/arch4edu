# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=sn
_pkgver=2.1.2
pkgname=r-${_pkgname,,}
pkgver=2.1.2
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
sha256sums=('2e801e3f74d970dd84c62badb0cb19ee53798016a7dd0b9840c53334f2583e66')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
