# system requirements: C++11
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=extraDistr
_pkgver=1.9.1
pkgname=r-${_pkgname,,}
pkgver=1.9.1
pkgrel=4
pkgdesc='Additional Univariate and Multivariate Distributions'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-rcpp
  gcc
)
optdepends=(
  r-actuar
  r-evd
  r-hoa
  r-laplacesdemon
  r-skellam
  r-testthat
  r-triangle
  r-vgam
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('9990348c4dbc611684fcb58ab8db7e856dfde1c9c86ffb7705f4b3dff6b2d7bf')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
