# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=logspline
_pkgver=2.1.17
pkgname=r-${_pkgname,,}
pkgver=2.1.17
pkgrel=1
pkgdesc='Routines for Logspline Density Estimation'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('Apache')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('03b72b860896f8801014b7b3b907389cc3cbe2e13bc1049241606df685a08815')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
