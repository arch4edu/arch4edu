# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_pkgname=purrr
_pkgver=1.1.0
pkgname=r-${_pkgname,,}
pkgver=1.1.0
pkgrel=1
pkgdesc='Functional Programming Tools'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-cli
  r-lifecycle
  r-magrittr
  r-rlang
  r-vctrs
)
optdepends=(
  r-covr
  r-dplyr
  r-httr
  r-knitr
  r-lubridate
  r-rmarkdown
  r-testthat
  r-tibble
  r-tidyselect
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('2ad28bff3b09a67fb3b81fb57d31c9903110e0e9e4fb76871245a35fa39c65b4')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
