# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggridges
_pkgver=0.5.6
pkgname=r-${_pkgname,,}
pkgver=0.5.6
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
sha256sums=('efccaa309a150d11c6b402b912e618ea041f25cca3101f32cd821a6f41684e35')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
