# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=philentropy
_pkgver=0.8.0
pkgname=r-${_pkgname,,}
pkgver=0.8.0
pkgrel=1
pkgdesc='Similarity and Distance Quantification Between Probability Functions'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-poorman
  r-rcpp
)
optdepends=(
  r-knitr
  r-microbenchmark
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('3aa6d4918168f4fe2c56ea3f26381b0ffc02f1d5b9b95e294bac1a34bf66be3e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
