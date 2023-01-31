# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggtext
_pkgver=0.1.2
pkgname=r-${_pkgname,,}
pkgver=0.1.2
pkgrel=1
pkgdesc="Improved Text Rendering Support for 'ggplot2'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-ggplot2
  r-gridtext
  r-rlang
  r-scales
)
optdepends=(
  r-cowplot
  r-dplyr
  r-glue
  r-knitr
  r-rmarkdown
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('8782171c44e5850e0c3a3c540e8db19b18b9b6e61b5ba5314dd7931d77cf7983')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
