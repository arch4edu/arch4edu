# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=urltools
_pkgver=1.7.3
pkgname=r-${_pkgname,,}
pkgver=1.7.3
pkgrel=4
pkgdesc='Vectorised Tools for URL Handling and Parsing'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-rcpp
  r-triebeard
)
optdepends=(
  r-knitr
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('6020355c1b16a9e3956674e5dea9ac5c035c8eb3eb6bbdd841a2b5528cafa313')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
