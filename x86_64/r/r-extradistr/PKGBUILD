# system requirements: C++11
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=extraDistr
_pkgver=1.10.0.5
pkgname=r-${_pkgname,,}
pkgver=1.10.0.5
pkgrel=1
pkgdesc='Additional Univariate and Multivariate Distributions'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-rcpp
  r-rcpparmadillo
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
sha256sums=('84014c85bd23cea3a9e19d87c061da3531a8e81c6c137b2b8e0db3d8c7f8636c')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
