# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggtext
_pkgver=0.2.0
pkgname=r-${_pkgname,,}
pkgver=0.2.0
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
sha256sums=('76b23e91c7565b0a6e1ba5adeb3ab976b3f3ccc80886841417afbe80f9af1a9e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
