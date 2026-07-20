# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=semPlot
_pkgver=1.2.0
pkgname=r-${_pkgname,,}
pkgver=1.2.0
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
sha256sums=('b47142bc8fbace70a5ce1a358fb85a2bd99a21cee20970da8b87725a6c6126e3')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
