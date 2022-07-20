# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=estimability
_pkgver=1.4
pkgname=r-${_pkgname,,}
pkgver=1.4
pkgrel=1
pkgdesc='Tools for Assessing Estimability of Linear Predictions'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('4a9eac160958457eeaf442e0bcd698990851b30a8963a3519f2d7da28b4bfa41')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
