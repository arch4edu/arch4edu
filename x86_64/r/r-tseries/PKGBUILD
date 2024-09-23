# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=tseries
_pkgver=0.10-58
pkgname=r-${_pkgname,,}
pkgver=0.10.58
pkgrel=1
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
sha256sums=('0edee71941bb8ea3d5ecad6b6a84d8019081f862138433b3c5e6fa5a4cbca724')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
