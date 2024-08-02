# system requirements: C++11
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=roxygen2
_pkgver=7.3.2
pkgname=r-${_pkgname,,}
pkgver=7.3.2
pkgrel=1
pkgdesc='In-Line Documentation for R'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-brew
  r-cli
  r-commonmark
  r-cpp11
  r-desc
  r-knitr
  r-pkgload
  r-purrr
  r-r6
  r-rlang
  r-stringi
  r-stringr
  r-withr
  r-xml2
)
optdepends=(
  r-covr
  r-r.methodss3
  r-r.oo
  r-rmarkdown
  r-testthat
  r-yaml
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('b788879f9132b7e2e656f442a6c592314676a9bf32d6a0a56e156cfa1ada011c')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
