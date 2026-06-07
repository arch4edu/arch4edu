# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=survminer
_pkgver=0.5.2
pkgname=r-${_pkgname,,}
pkgver=0.5.2
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
sha256sums=('17c958645fb842a2ae9c61b22721b2684b372f296ee2c2cca8381afcdc0d08c1')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
