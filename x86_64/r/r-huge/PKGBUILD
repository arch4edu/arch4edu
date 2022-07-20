# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=huge
_pkgver=1.3.5
pkgname=r-${_pkgname,,}
pkgver=1.3.5
pkgrel=4
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
sha256sums=('9240866e2f773cd0ac8a02514871149d2babaa162a49e151eab9591ad42984ea')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
