# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=NetworkToolbox
_pkgver=1.4.4
pkgname=r-${_pkgname,,}
pkgver=1.4.4
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
sha256sums=('7493462e9269ce74a9c2d5aa853bf85b4160aca021906505bd509a0b51b7ccc7')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
