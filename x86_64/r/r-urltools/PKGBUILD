# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=urltools
_pkgver=1.7.3.1
pkgname=r-${_pkgname,,}
pkgver=1.7.3.1
pkgrel=1
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
sha256sums=('f85bb761bb85beef98d34cef0030b589bb71c24cfebc1959b5954fb0676c8772')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
