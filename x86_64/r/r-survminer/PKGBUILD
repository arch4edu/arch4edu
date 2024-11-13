# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=survminer
_pkgver=0.5.0
pkgname=r-${_pkgname,,}
pkgver=0.5.0
pkgrel=1
pkgdesc="Drawing Survival Curves using 'ggplot2'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-broom
  r-dplyr
  r-ggplot2
  r-ggpubr
  r-ggtext
  r-gridextra
  r-magrittr
  r-maxstat
  r-purrr
  r-rlang
  r-scales
  r-survmisc
  r-tibble
  r-tidyr
)
optdepends=(
  r-cmprsk
  r-flexsurv
  r-knitr
  r-markdown
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('d2c7117d1ebce79b1e2b5512f35f53c2aa0702bbb4d5761c145e0d2e4893f58b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
