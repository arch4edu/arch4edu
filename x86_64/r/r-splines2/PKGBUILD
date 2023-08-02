# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=splines2
_pkgver=0.5.0
pkgname=r-${_pkgname,,}
pkgver=0.5.0
pkgrel=1
pkgdesc='Regression Spline Functions and Classes'
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
  r-rcpparmadillo
  r-rmarkdown
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('fbef2d935d051a175892a6f2c48ce8bd574459614f9fc7faee82653dc048d7d5')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
