# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=sna
_pkgver=2.8
pkgname=r-${_pkgname,,}
pkgver=2.8
pkgrel=1
pkgdesc='Tools for Social Network Analysis'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-network
  r-statnet.common
)
optdepends=(
  r-numderiv
  r-rgl
  r-sparsem
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('f20adb8e505cd56ae9ed0d9675337b4fab15d5dbad1bff3562edd971872a994c')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
