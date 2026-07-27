# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=huge
_pkgver=2.0.0
pkgname=r-${_pkgname,,}
pkgver=2.0.0
pkgrel=1
pkgdesc='High-Dimensional Undirected Graph Estimation'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-igraph
  r-rcpp
  r-rcppeigen
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('c5987c535b27d2678cdfab10014404cf860fef393ad433ba10f16bec0aaaa725')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
