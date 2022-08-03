# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=semPlot
_pkgver=1.1.5
pkgname=r-${_pkgname,,}
pkgver=1.1.5
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
sha256sums=('6cd39e6f80cf9e5c5045e7f8f2e888ea1b0355e084909b1b1c1ddac4b04ffb34')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
