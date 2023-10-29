# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=urca
_pkgver=1.3-3
pkgname=r-${_pkgname,,}
pkgver=1.3.3
pkgrel=1
pkgdesc='Unit Root and Cointegration Tests for Time Series Data'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('43baa8b6735f8325a69e6a43686f4fecd77a0eb7f60da25b4fc5c51b9271e9f1')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
