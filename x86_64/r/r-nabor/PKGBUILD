# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=nabor
_pkgver=0.5.0
pkgname=r-${_pkgname,,}
pkgver=0.5.0
pkgrel=4
pkgdesc="Wraps 'libnabo', a Fast K Nearest Neighbour Library for Low Dimensions"
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('BSD')
depends=(
  r
  r-bh
  r-rcpp
  r-rcppeigen
)
optdepends=(
  r-rann
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('47938dcc987279281c13abfd667660bf1b3b76af116136a27eb066ee1a4b43da')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
