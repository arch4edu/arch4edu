# system requirements: C++11
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=roxygen2
_pkgver=8.1.0
pkgname=r-${_pkgname,,}
pkgver=8.1.0
pkgrel=2
pkgdesc='In-Line Documentation for R'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r-brew
  r-cli
  r-commonmark
  r-desc
  r-knitr
  r-lifecycle
  r-pkgload
  r-r6
  r-rdtools
  r-rlang
  r-withr
  r-xml2
)
makedepends=(
  r-cpp11
)
optdepends=(
  r-covr
  r-r.methodss3
  r-r.oo
  r-rmarkdown
  r-s7
  r-testthat
  r-yaml
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('6ee35d555ba8cfdbb0ab9c419e4f4af03e6a7acd8a0eaa77bc31fd50941fb691')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
