# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggridges
_pkgver=0.5.3
pkgname=r-${_pkgname,,}
pkgver=0.5.3
pkgrel=4
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
sha256sums=('f5eafab17f2d4a8a2a83821ad3e96ae7c26b62bbce9de414484c657383c7b42e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
