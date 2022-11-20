# system requirements: C++11
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=mice
_pkgver=3.15.0
pkgname=r-${_pkgname,,}
pkgver=3.15.0
pkgrel=1
pkgdesc='Multivariate Imputation by Chained Equations'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-broom
  r-cpp11
  r-dplyr
  r-generics
  r-rcpp
  r-rlang
  r-tidyr
  r-withr
  gcc
)
optdepends=(
  r-broom.mixed
  r-decor
  r-glmnet
  r-haven
  r-knitr
  r-lme4
  r-lmtest
  r-mass
  r-metafor
  r-miceadds
  r-mitml
  r-nnet
  r-pan
  r-randomforest
  r-ranger
  r-rmarkdown
  r-rpart
  r-survival
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('3d64dd260e3dce9c4c2f7be8c99f3063769df9ccfd3a0fc827c2de0ac842e87b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
