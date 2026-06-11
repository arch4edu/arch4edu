# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=mixOmics
_pkgver=6.32.0
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
  r-gsignal
  r-igraph
  r-matrixstats
  r-rarpack
  r-rcolorbrewer
  r-reshape2
  r-rgl
  r-tidyr
)
optdepends=(
  r-biocstyle
  r-knitr
  r-magick
  r-microbenchmark
  r-rmarkdown
  r-testthat
  r-mime
  r-vdiffr
  r-kableextra
  r-devtools
)
source=("https://bioconductor.org/packages/release/bioc/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f2e3e8336ac86af54e7ea0c3b3b7f47a')
b2sums=('47526ae081796f33b83ed01de10f4b1757496ccfde4b4ff92b4792076482067a67aacaecc9efe7f10133c70f2d85fc36b87a8e590124d79d56617b58c53f6e5f')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
