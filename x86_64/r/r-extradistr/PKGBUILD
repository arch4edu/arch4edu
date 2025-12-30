# system requirements: C++11
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=extraDistr
_pkgver=1.10.0.1
pkgname=r-${_pkgname,,}
pkgver=1.10.0.1
pkgrel=1
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
sha256sums=('b55feaddb5f5d47d7842977271a03eb881306fc03564146116c09c3810832074')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
