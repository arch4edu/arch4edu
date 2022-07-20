# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=shape
_pkgver=1.4.6
pkgname=r-${_pkgname,,}
pkgver=1.4.6
pkgrel=4
pkgdesc='Functions for Plotting Graphical Shapes, Colors'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('b9103e5ed05c223c8147dbe3b87a0d73184697343634a353a2ae722f7ace0b7b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
