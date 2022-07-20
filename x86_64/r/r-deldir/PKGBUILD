# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=deldir
_pkgver=1.0-6
pkgname=r-${_pkgname,,}
pkgver=1.0.6
pkgrel=4
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
sha256sums=('6df6d8325c607e0b7d63cbc53c29e774eff95ad4acf9c7ec8f70693b0505f8c5')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
