# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=profvis
_pkgver=0.4.0
pkgname=r-${_pkgname,,}
pkgver=0.4.0
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
sha256sums=('d2fdeb0e6021f4dfc7c0634bec818cd82a6baf8042b80a1818aae0caa6bf4cf4')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
