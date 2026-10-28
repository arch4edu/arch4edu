# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=NetworkToolbox
_pkgver=1.5.0
pkgname=r-${_pkgname,,}
pkgver=1.5.0
pkgrel=1
pkgdesc='Methods and Measures for Brain, Cognitive, and Psychometric Network Analysis'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-corrplot
  r-doparallel
  r-fdrtool
  r-foreach
  r-igraph
  r-isingfit
  r-pbapply
  r-ppcor
  r-psych
  r-pwr
  r-qgraph
  r-r.matlab
)
optdepends=(
  r-googledrive
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('b5fe93700d9afcbd524701f24a2f869359cb39b6e44b187c68e0a3d612e6352c')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
