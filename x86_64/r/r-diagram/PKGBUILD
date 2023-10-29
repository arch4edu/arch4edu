# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=diagram
_pkgver=1.6.5
pkgname=r-${_pkgname,,}
pkgver=1.6.5
pkgrel=4
pkgdesc='Functions for Visualising Simple Graphs (Networks), Plotting Flow Diagrams'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-shape
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('e9c03e7712e0282c5d9f2b760bafe2aac9e99a9723578d9e6369d60301f574e4')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
