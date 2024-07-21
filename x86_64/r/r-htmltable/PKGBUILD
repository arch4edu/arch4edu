# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=htmlTable
_pkgver=2.4.3
pkgname=r-${_pkgname,,}
pkgver=2.4.3
pkgrel=1
pkgdesc='Advanced Tables for Markdown/HTML'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-checkmate
  r-htmltools
  r-htmlwidgets
  r-knitr
  r-magrittr
  r-rstudioapi
  r-stringr
)
optdepends=(
  r-chron
  r-dplyr
  r-glue
  r-hmisc
  r-lubridate
  r-purrr
  r-reshape
  r-rlang
  r-rmarkdown
  r-testthat
  r-tibble
  r-tidyr
  r-tidyselect
  r-xml
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('3739d01bff313ccd206b63940a8252b037f0521d041c721a4e0d195abd6ef6dd')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
