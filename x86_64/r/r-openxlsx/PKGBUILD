# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=openxlsx
_pkgver=4.2.5.2
pkgname=r-${_pkgname,,}
pkgver=4.2.5.2
pkgrel=1
pkgdesc='Read, Write and Edit xlsx Files'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-rcpp
  r-stringi
  r-zip
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-roxygen2
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('ee7089e7e5832ef22ee0d0eebf7cca5096ce23afb2bcdb58700be62526fc9b67')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
