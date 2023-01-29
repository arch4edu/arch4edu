# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=sna
_pkgver=2.7-1
pkgname=r-${_pkgname,,}
pkgver=2.7.1
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
sha256sums=('60daf217c15b6fa335804600dc1e6eb73594b6e794faa4f82a2275c4d8570ae3')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
