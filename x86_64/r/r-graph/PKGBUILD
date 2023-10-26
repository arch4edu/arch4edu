# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=graph
_pkgver=1.80.0
pkgname=r-${_pkgname,,}
pkgver=1.80.0
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
sha256sums=('017446e90386aba89d2326d30006db14d191bc9b4ce916e0d0ebd979a73fef5c')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
