# system requirements: C++14
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=glmnet
_pkgver=4.1-4
pkgname=r-${_pkgname,,}
pkgver=4.1.4
pkgrel=5
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
sha256sums=('f6b0f70a0b3d81ff91c2b94f795a2a32e90dd458270f1a29e49e085dd65000f9')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
