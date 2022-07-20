# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=quadprog
_pkgver=1.5-8
pkgname=r-${_pkgname,,}
pkgver=1.5.8
pkgrel=4
pkgdesc='Functions to Solve Quadratic Programming Problems'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('22128dd6b08d3516c44ff89276719ad4fe46b36b23fdd585274fa3a93e7a49cd')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
