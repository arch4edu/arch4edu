# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=semPlot
_pkgver=1.1.7
pkgname=r-${_pkgname,,}
pkgver=1.1.7
pkgrel=1
pkgdesc="Path Diagrams and Visual Analysis of Various SEM Packages' Output"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-colorspace
  r-corpcor
  r-igraph
  r-lavaan
  r-lisreltor
  r-openmx
  r-plyr
  r-qgraph
  r-rockchalk
  r-sem
  r-xml
)
optdepends=(
  r-mplusautomation
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('56921be740f967884ff3af69377fd17e8bfef1bfe582c86399e64c5dabab4ca2')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
