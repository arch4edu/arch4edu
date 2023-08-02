# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=profvis
_pkgver=0.3.8
pkgname=r-${_pkgname,,}
pkgver=0.3.8
pkgrel=1
pkgdesc='Interactive Visualizations for Profiling R Code'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-htmlwidgets
  r-purrr
  r-rlang
  r-stringr
  r-vctrs
)
optdepends=(
  r-devtools
  r-ggplot2
  r-htmltools
  r-knitr
  r-rmarkdown
  r-shiny
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('ec02c75bc9907a73564e691adfa8e06651ca0bd73b7915412960231cd265b4b2')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
