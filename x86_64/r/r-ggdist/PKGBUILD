# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggdist
_pkgver=3.3.0
pkgname=r-${_pkgname,,}
pkgver=3.3.0
pkgrel=1
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
  r-quadprog
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
sha256sums=('1441a6dae5bc4b084a741a6f8782a13235171013cc028bf1d694662e4e5a252c')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
