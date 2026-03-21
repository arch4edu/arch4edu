# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ade4
_pkgver=1.7-24
pkgname=r-${_pkgname,,}
pkgver=1.7.24
pkgrel=1
pkgdesc='Analysis of Ecological Data: Exploratory and Euclidean Methods in Environmental Sciences'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-pixmap
  r-rcpp
  r-rcpparmadillo
  r-sp
)
optdepends=(
  r-ade4tkgui
  r-adegraphics
  r-adephylo
  r-ape
  r-circstats
  r-deldir
  r-doparallel
  r-foreach
  r-iterators
  r-lattice
  r-parallel
  r-progress
  r-spdep
  r-splancs
  r-waveslim
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('59509dcf781b2b69a97e225f53f2f76d0e0d5bfb04c5b6198007c035c4bd6d2a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
