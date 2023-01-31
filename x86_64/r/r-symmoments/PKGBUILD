# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=symmoments
_pkgver=1.2.1
pkgname=r-${_pkgname,,}
pkgver=1.2.1
pkgrel=1
pkgdesc='Symbolic Central and Noncentral Moments of the Multivariate Normal Distribution'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-combinat
  r-cubature
  r-multipol
  r-mvtnorm
)
optdepends=(
  r-ape
  r-mpoly
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('9a6be1f8fe44f6ab5a1790e870fd8b18de1686a48a14a9fca2d035bfb5458672')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
