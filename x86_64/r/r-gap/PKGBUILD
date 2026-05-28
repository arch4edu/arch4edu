# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gap
_pkgver=1.15.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Genetic Analysis Package"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-dplyr
  r-gap.datasets
  r-ggplot2
  r-plotly
  r-rdpack
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-bdsmatrix
  r-bookdown
  r-bradleyterry2
  r-calibrate
  r-circlize
  r-coda
  r-cowplot
  r-coxme
  r-diagrammer
  r-genetics
  r-haplo.stats
  r-htmltools
  r-htmlwidgets
  r-jsonlite
  r-kinship2
  r-knitr
  r-magic
  r-matrixstats
  r-mcmcglmm
  r-meta
  r-metafor
  r-pedigree
  r-pedigreemm
  r-plotrix
  r-r2jags
  r-readr
  r-reshape
  r-rmarkdown
  r-rms
  r-scales
  r-valr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('52478515ea26137597b2010a69d0a738')
b2sums=('7b059b3dbf0505430d61f9ee3fa7301e5da31c4af594cee8831bae5f35aeffd061f012fd269eaf3334be9bd082f7ba0733544fafffa4ab2a8cbe0544fbaa0e30')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
