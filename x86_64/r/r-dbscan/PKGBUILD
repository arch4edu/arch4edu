# system requirements: C++11
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=dbscan
_pkgver=1.1-11
pkgname=r-${_pkgname,,}
pkgver=1.1.11
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
sha256sums=('f0498e67e612629340a2758fbe747c4d9d4ca648f002230a03499cb73735e62f')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
