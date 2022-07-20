# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=tseries
_pkgver=0.10-51
pkgname=r-${_pkgname,,}
pkgver=0.10.51
pkgrel=1
pkgdesc='Time Series Analysis and Computational Finance'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-quadprog
  r-quantmod
  r-zoo
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('a55f20704883710ab58ea479e20cf0f263c50d54282f693793cda4af664c207f')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
