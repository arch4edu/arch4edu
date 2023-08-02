# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Maintainer: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=SQUAREM
_pkgver=2021.1
pkgname=r-${_pkgname,,}
pkgver=2021.1
pkgrel=10
pkgdesc='Squared Extrapolation Methods for Accelerating EM-Like Monotone Algorithms'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-setrng
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('66e5e18ca29903e4950750bbd810f0f9df85811ee4195ce0a86d939ba8183a58')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
