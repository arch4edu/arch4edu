# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggalluvial
_pkgver=0.12.4
pkgname=r-${_pkgname,,}
pkgver=0.12.4
pkgrel=1
pkgdesc="Alluvial Plots in 'ggplot2'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-dplyr
  r-ggplot2
  r-lazyeval
  r-rlang
  r-tidyr
  r-tidyselect
)
optdepends=(
  r-alluvial
  r-babynames
  r-ggfittext
  r-ggrepel
  r-grid
  r-htmltools
  r-knitr
  r-rmarkdown
  r-sessioninfo
  r-shiny
  r-sp
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('e3ffc55fa2e78d3c4ffd528ef48ad471b3b30a154a8c56d3239465a91f975674')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
