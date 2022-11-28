# system requirements: C++14
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=glmnet
_pkgver=4.1-6
pkgname=r-${_pkgname,,}
pkgver=4.1.6
pkgrel=1
pkgdesc='Lasso and Elastic-Net Regularized Generalized Linear Models'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-foreach
  r-rcpp
  r-rcppeigen
  r-shape
  gcc
)
optdepends=(
  r-knitr
  r-lars
  r-rmarkdown
  r-testthat
  r-xfun
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('bec4c6cea284d0dc24bbdac3e623f0772cea1d74ef77e718651e3830c74b7e30')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
