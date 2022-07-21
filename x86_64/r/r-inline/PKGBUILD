# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=inline
_pkgver=0.3.19
pkgname=r-${_pkgname,,}
pkgver=0.3.19
pkgrel=4
pkgdesc='Functions to Inline C, C++, Fortran Function Calls from R'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('LGPL')
depends=(
  r
)
optdepends=(
  r-rcpp
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('0ee9309bb7dab0b97761ddd18381aa12bd7d54678ccd7bec00784e831f4c99d5')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
