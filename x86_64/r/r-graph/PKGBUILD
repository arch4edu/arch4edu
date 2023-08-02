# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=graph
_pkgver=1.78.0
pkgname=r-${_pkgname,,}
pkgver=1.78.0
pkgrel=1
pkgdesc='graph: A package to handle graph data structures'
arch=('x86_64')
url="https://bioconductor.org/packages/${_pkgname}"
license=('Artistic2.0')
depends=(
  r
  r-biocgenerics
)
optdepends=(
  r-biocstyle
  r-cluster
  r-knitr
  r-rbgl
  r-rgraphviz
  r-runit
  r-sparsem
  r-xml
)
source=("https://bioconductor.org/packages/release/bioc/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('5667e2d29dc4646bc57880ae28f7fdc9d589aeb41173c4147bea2ec4faff91a0')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
