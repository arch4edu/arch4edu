# system requirements: gmp (>= 4.38, optional), libxml2 (optional), glpk(optional)
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=igraph
_pkgver=1.3.5
pkgname=r-${_pkgname,,}
pkgver=1.3.5
pkgrel=3
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
sha256sums=('9e615d67b6b5b57dfa54ec2bbc8c29da8f7c3fe82af1e35ab27273b1035b9bd4')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
