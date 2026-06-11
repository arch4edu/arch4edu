# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=RcppML
_pkgver=0.3.7.1
pkgname=r-${_pkgname,,}
pkgver=0.3.7.1
pkgrel=1
pkgdesc='Rcpp Machine Learning Library'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-rcpp
  r-rcppeigen
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('9a2e2556b436504b270ac29b31d7a72c07fe5f34d48562e5930366fb228aae4b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
