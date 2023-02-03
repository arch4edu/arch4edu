# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=ggrepel
_pkgver=0.9.3
pkgname=r-${_pkgname,,}
pkgver=0.9.3
pkgrel=1
pkgdesc="Automatically Position Non-Overlapping Text Labels with 'ggplot2'"
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-ggplot2
  r-rcpp
  r-rlang
  r-scales
)
optdepends=(
  r-devtools
  r-dplyr
  r-ggbeeswarm
  r-gridextra
  r-knitr
  r-magrittr
  r-prettydoc
  r-readr
  r-rmarkdown
  r-stringr
  r-svglite
  r-testthat
  r-vdiffr
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('b9eba0e2edee84db0276b49e4834b65f5369edc4bc56f4cacc13e0d1c39a005c')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
