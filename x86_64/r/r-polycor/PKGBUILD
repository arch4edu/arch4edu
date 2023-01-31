# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=polycor
_pkgver=0.8-1
pkgname=r-${_pkgname,,}
pkgver=0.8.1
pkgrel=3
pkgdesc='Polychoric and Polyserial Correlations'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-admisc
  r-mvtnorm
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('f05f53e0b5c992de0e5b4c6b2e998148cf83310358821e1bba180d81face0509')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
