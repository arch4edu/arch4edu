# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=checkmate
_pkgver=2.1.0
pkgname=r-${_pkgname,,}
pkgver=2.1.0
pkgrel=8
pkgdesc='Fast and Versatile Argument Checks'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('BSD')
depends=(
  r
  r-backports
)
optdepends=(
  r-data.table
  r-devtools
  r-fastmatch
  r-ggplot2
  r-knitr
  r-magrittr
  r-microbenchmark
  r-r6
  r-rmarkdown
  r-testthat
  r-tibble
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('b784dd5163a0350d084ef34882d9781373839dedeaa9a8b8e6187d773d0d21c6')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
