# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=symmoments
_pkgver=1.2.1.1
pkgname=r-${_pkgname,,}
pkgver=1.2.1.1
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
sha256sums=('00c9bca2585c2a1ef9b6cc45e2da27117c622f4dc27a3c0b90c91decedc94fc4')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
