# system requirements: GNU Make, C++11
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Boom
_pkgver=0.9.11
pkgname=r-${_pkgname,,}
pkgver=0.9.11
pkgrel=1
pkgdesc='Bayesian Object Oriented Modeling'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('LGPL')
depends=(
  r
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('7185c0f91b62c382ce1ad922b6b298611ecac1655433fe307b337da1e81e779e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
