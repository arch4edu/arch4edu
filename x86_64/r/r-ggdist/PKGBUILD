# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggdist
_pkgver=3.2.0
pkgname=r-${_pkgname,,}
pkgver=3.2.0
pkgrel=4
pkgdesc='Visualizations of Distributions and Uncertainty'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-distributional
  r-dplyr
  r-ggplot2
  r-glue
  r-hdinterval
  r-numderiv
  r-rlang
  r-scales
  r-tibble
  r-tidyselect
  r-vctrs
  r-withr
)
optdepends=(
  r-beeswarm
  r-broom
  r-covr
  r-cowplot
  r-fda
  r-forcats
  r-gdtools
  r-knitr
  r-modelr
  r-palmerpenguins
  r-patchwork
  r-pkgdown
  r-png
  r-posterior
  r-purrr
  r-rmarkdown
  r-svglite
  r-testthat
  r-tidyr
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('09c989d9ebb282d6eaae37f68a8c98abce61d9788527e691ed2ebe42da111e46')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
