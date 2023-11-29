# system requirements: C++11
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=dbscan
_pkgver=1.1-12
pkgname=r-${_pkgname,,}
pkgver=1.1.12
pkgrel=1
pkgdesc='Density Based Clustering of Applications with Noise (DBSCAN) and Related Algorithms'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-rcpp
  gcc
)
optdepends=(
  r-dendextend
  r-fpc
  r-igraph
  r-knitr
  r-microbenchmark
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('56f8b1bdb392f8fb679a343b2ad5b4656c4f21d4ead85d6d81900d2f8b63ceea')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
