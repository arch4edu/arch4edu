# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=semTools
_pkgver=0.5-8
pkgname=r-${_pkgname,,}
pkgver=0.5.8
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
sha256sums=('4092d156ee89ac6b684c71916535e423bed115d0c89395563c30de003f52384f')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
