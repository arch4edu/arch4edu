# system requirements: gmp (>= 4.38, optional), libxml2 (optional), glpk(optional)
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=igraph
_pkgver=1.4.0
pkgname=r-${_pkgname,,}
pkgver=1.4.0
pkgrel=1
pkgdesc='Network Analysis and Visualization'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-magrittr
  r-pkgconfig
  r-rlang
)
optdepends=(
  glpk
  gmp
  libxml2
  r-ape
  r-digest
  r-graph
  r-igraphdata
  r-rgl
  r-scales
  r-stats4
  r-tcltk
  r-testthat
  r-withr
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('c3923e6fbb96104cabc31dc7fcb53e3956687fa2c83743c561a798c8e355fa6d')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
