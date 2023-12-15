# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggridges
_pkgver=0.5.5
pkgname=r-${_pkgname,,}
pkgver=0.5.5
pkgrel=1
pkgdesc="Ridgeline Plots in 'ggplot2'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-ggplot2
  r-scales
  r-withr
)
optdepends=(
  r-covr
  r-dplyr
  r-forcats
  r-ggplot2movies
  r-knitr
  r-patchwork
  r-rmarkdown
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('7577a43824ff413f5499fce22b2218268177d5867adf8cb885a19c760b5e75a1')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
