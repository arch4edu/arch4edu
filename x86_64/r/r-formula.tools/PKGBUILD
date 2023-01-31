# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=formula.tools
_pkgver=1.7.1
pkgname=r-${_pkgname,,}
pkgver=1.7.1
pkgrel=7
pkgdesc='Programmatic Utilities for Manipulating Formulas, Expressions, Calls, Assignments and Other R Objects'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-operator.tools
)
optdepends=(
  r-magrittr
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('4fe0e72d9d96f2398e86cbd8536d0c84de38e5583d4ff7dcd73f415ddd8ca395')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
