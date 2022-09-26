# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggridges
_pkgver=0.5.4
pkgname=r-${_pkgname,,}
pkgver=0.5.4
pkgrel=1
pkgdesc="Ridgeline Plots in 'ggplot2'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-ggplot2
  r-plyr
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
sha256sums=('2bf71c2034804cec637e6748dc51d8cadad01d3ea4d14ace754327f082e8d851')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
