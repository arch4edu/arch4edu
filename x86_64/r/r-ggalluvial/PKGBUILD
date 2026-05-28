# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggalluvial
_pkgver=0.12.6
pkgname=r-${_pkgname,,}
pkgver=0.12.6
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
sha256sums=('f0397b18c43ed1e085c7bc1bbab3b81b46005ff3f420a635e903729083949d51')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
