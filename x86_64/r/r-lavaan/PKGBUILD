# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=lavaan
_pkgver=0.7-3
pkgname=r-${_pkgname,,}
pkgver=0.7.3
pkgrel=1
pkgdesc='Latent Variable Analysis'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-mnormt
  r-numderiv
  r-pbivnorm
  r-quadprog
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('c1e9ecbd01dde0ada6bda11f0f9e84babfefebf06d1ab5887b4bd8d24ebb6787')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
