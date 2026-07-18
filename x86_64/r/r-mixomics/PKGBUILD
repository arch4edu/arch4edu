# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=mixOmics
_pkgver=6.36.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Omics Data Integration Project"
arch=(any)
url="https://bioconductor.org/packages/$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-biocparallel
  r-corpcor
  r-dplyr
  r-ellipse
  r-ggplot2
  r-ggrepel
  r-gridextra
  r-igraph
  r-matrixstats
  r-rarpack
  r-rcolorbrewer
  r-reshape2
  r-rgl
  r-rlang
  r-tidyr
)
optdepends=(
  r-biocstyle
  r-devtools
  r-kableextra
  r-knitr
  r-magick
  r-microbenchmark
  r-mime
  r-rmarkdown
  r-testthat
  r-vdiffr
)
source=("https://bioconductor.org/packages/release/bioc/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('fcae304a8d7a390f8ad20143c890b2c8')
b2sums=('0f7ca62d08d462d9d4e526d8f62a0e4168cd843ef442381b5bd956c47f797bf67f6df802d0a509e8c6c15487ec75f45a0286c6d0d4ec2fa673c7f48eb36602b7')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
