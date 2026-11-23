# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gridExtra
_pkgver=2.3.1
pkgname=r-${_pkgname,,}
pkgver=2.3.1
pkgrel=1
pkgdesc='Miscellaneous Functions for "Grid" Graphics'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-gtable
)
optdepends=(
  r-egg
  r-ggplot2
  r-knitr
  r-lattice
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('de42e501ac2c6a70bd0ffc18d7703e9b0e6b878c610df09756183c3e52445c82')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
