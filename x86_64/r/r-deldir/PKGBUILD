# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=deldir
_pkgver=2.0-4
pkgname=r-${_pkgname,,}
pkgver=2.0.4
pkgrel=1
pkgdesc='Delaunay Triangulation and Dirichlet (Voronoi) Tessellation'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-polyclip
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('d418acb28ec3707b6d64c7466d0cefbb49b098537f37558d8f7a5befd34a4653')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
