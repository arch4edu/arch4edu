# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=RcppDist
_pkgver=0.1.1.1
pkgname=r-${_pkgname,,}
pkgver=0.1.1.1
pkgrel=1
pkgdesc="'Rcpp' Integration of Additional Probability Distributions"
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-rcpp
  r-rcpparmadillo
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('aefd99dd207b9b545cf6070078bb9dd7f4ba51049063f3324e9849c7131b09ae')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
