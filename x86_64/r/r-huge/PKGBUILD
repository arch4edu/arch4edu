# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=huge
_pkgver=1.6
pkgname=r-${_pkgname,,}
pkgver=1.6
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
sha256sums=('d71a72512b4c5815d70f1cde6cb8bc7f519e79651ee2bdf4e1fca6cf84b485ce')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
