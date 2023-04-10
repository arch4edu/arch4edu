# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Rcsdp
_pkgver=0.1.57.5
pkgname=r-${_pkgname,,}
pkgver=0.1.57.5
pkgrel=1
pkgdesc='R Interface to the CSDP Semidefinite Programming Library'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('CPL')
depends=(
  r
)
optdepends=(
  r-matrix
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('50048bcb4a8bb9f9b48c5e43a32126eda1d23d17876c7632e20b04953f3b1cd2')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
