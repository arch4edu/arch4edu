# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=plotly
_pkgver=4.11.0
pkgname=r-${_pkgname,,}
pkgver=4.11.0
pkgrel=1
pkgdesc="Create Interactive Web Graphics via 'plotly.js'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-base64enc
  r-crosstalk
  r-data.table
  r-digest
  r-dplyr
  r-ggplot2
  r-htmltools
  r-htmlwidgets
  r-httr
  r-jsonlite
  r-lazyeval
  r-magrittr
  r-promises
  r-purrr
  r-rcolorbrewer
  r-rlang
  r-scales
  r-tibble
  r-tidyr
  r-vctrs
  r-viridislite
)
optdepends=(
  r-broom
  r-cairo
  r-curl
  r-dendextend
  r-forcats
  r-ggalluvial
  r-ggally
  r-ggthemes
  r-hexbin
  r-irdisplay
  r-knitr
  r-listviewer
  r-maps
  r-mass
  r-palmerpenguins
  r-plotlygeoassets
  r-png
  r-processx
  r-reticulate
  r-rmarkdown
  r-rsvg
  r-rversions
  r-sf
  r-shiny
  r-shinytest
  r-testthat
  r-webshot
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('ba9009cd7e913590872aa153b13be719e4dfcee8cd24f8631bd35c99044bceb3')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
