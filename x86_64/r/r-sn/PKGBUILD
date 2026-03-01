# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=sn
_pkgver=2.1.3
pkgname=r-${_pkgname,,}
pkgver=2.1.3
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
sha256sums=('144df1ad03d28acd06f1231dd6efa9638db930402818a380b5b0f08eee816218')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
