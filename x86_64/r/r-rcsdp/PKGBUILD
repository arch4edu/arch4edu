# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Rcsdp
_pkgver=0.1.57.4
pkgname=r-${_pkgname,,}
pkgver=0.1.57.4
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
sha256sums=('4a317a7cff4edfa439239dbb0de0f5a0287b1af7f91ef6e96cdc815597ab4b3e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
