# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=tseries
_pkgver=0.10-54
pkgname=r-${_pkgname,,}
pkgver=0.10.54
pkgrel=3
pkgdesc='Time Series Analysis and Computational Finance'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-jsonlite
  r-quadprog
  r-quantmod
  r-zoo
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('c3ca3263b58a22dd9f613b0be34a6f401caa9c88f0609c0b4e825f1efab4d028')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
