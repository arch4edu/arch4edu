# system requirements: C++11
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=roxygen2
_pkgver=7.2.3
pkgname=r-${_pkgname,,}
pkgver=7.2.3
pkgrel=3
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
sha256sums=('d844fab977d2575ab942fa1309ac7ff67f35f099a75d8b41c79efe6ea10416da')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
