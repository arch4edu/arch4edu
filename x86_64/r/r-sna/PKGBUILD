# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=sna
_pkgver=2.7
pkgname=r-${_pkgname,,}
pkgver=2.7
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
sha256sums=('440fa4347c7b437e93c73127d34894068afd240d3128898474a7201e740a434d')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
