# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=bsts
_pkgver=0.9.8
pkgname=r-${_pkgname,,}
pkgver=0.9.8
pkgrel=1
pkgdesc='Bayesian Structural Time Series'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('LGPL')
depends=(
  r
  r-boom
  r-boomspikeslab
  r-xts
  r-zoo
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('8c8ef3cd2bdb6d23fe72c74971ceb88847d215091bdc76fae3765f9b99430090')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
