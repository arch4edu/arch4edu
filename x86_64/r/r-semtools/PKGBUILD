# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=semTools
_pkgver=0.5-10
pkgname=r-${_pkgname,,}
pkgver=0.5.10
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
sha256sums=('338ec536c76d0f084089f54fe71362c28786a94868d538741c84a3ede2e247ad')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
