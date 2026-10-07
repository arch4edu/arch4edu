# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=symmoments
_pkgver=1.2.2
pkgname=r-${_pkgname,,}
pkgver=1.2.2
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
  r-mpoly
  r-rdpack
)
optdepends=(
  r-ape

)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('5a95ba3a27ba455c7e9f0f541a58a7e4ee5c715829dbba99e4008fbbe788adee')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
