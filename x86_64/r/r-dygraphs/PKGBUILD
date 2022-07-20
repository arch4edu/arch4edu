# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=dygraphs
_pkgver=1.1.1.6
pkgname=r-${_pkgname,,}
pkgver=1.1.1.6
pkgrel=5
pkgdesc="Interface to 'Dygraphs' Interactive Time Series Charting Library"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-htmltools
  r-htmlwidgets
  r-magrittr
  r-xts
  r-zoo
)
optdepends=(
  r-rmarkdown
  r-shiny
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('c3d331f30012e721a048e04639f60ea738cd7e54e4f930ac9849b95f0f005208')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
