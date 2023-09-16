# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gnm
_pkgver=1.1-5
pkgname=r-${_pkgname,,}
pkgver=1.1.5
pkgrel=1
pkgdesc='Generalized Nonlinear Models'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-qvcalc
  r-relimp
)
optdepends=(
  r-testthat
  r-vcdextra
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('44d94ef3785cf8a070a1d816698e5ec726b506bbc6b73c18e661d6a64dfdf845')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
