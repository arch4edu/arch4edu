# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=semTools
_pkgver=0.5-9
pkgname=r-${_pkgname,,}
pkgver=0.5.9
pkgrel=1
pkgdesc='Useful Tools for Structural Equation Modeling'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-lavaan
  r-pbivnorm
)
optdepends=(
  r-amelia
  r-blavaan
  r-emmeans
  r-foreign
  r-gparotation
  r-mass
  r-mice
  r-mnormt
  r-parallel
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('8de79f0b2c4ff07e11254d60d6a3918b36beb5b5323e64be8f0bfe6d18f1ade5')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
