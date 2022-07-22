# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=colourpicker
_pkgver=1.1.1
pkgname=r-${_pkgname,,}
pkgver=1.1.1
pkgrel=4
pkgdesc='A Colour Picker Tool for Shiny and for Selecting Colours in Plots'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-ggplot2
  r-htmltools
  r-htmlwidgets
  r-jsonlite
  r-miniui
  r-shiny
  r-shinyjs
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-rstudioapi
  r-shinydisconnect
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('a0d09982b048b143e2c3438ccec039dd20d6f892fa0dedc9fdcb0d40de883ce0')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
