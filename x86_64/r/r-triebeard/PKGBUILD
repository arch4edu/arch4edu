# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=triebeard
_pkgver=0.3.0
pkgname=r-${_pkgname,,}
pkgver=0.3.0
pkgrel=4
pkgdesc="'Radix' Trees in 'Rcpp'"
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-rcpp
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('bf1dd6209cea1aab24e21a85375ca473ad11c2eff400d65c6202c0fb4ef91ec3')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
