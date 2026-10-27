# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gap
_pkgver=1.15.3
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
  r-remotes
  r-reshape
  r-rmarkdown
  r-rms
  r-scales
  r-testthat
  r-valr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('bb89c9d8d40e2f9d032135fce41c8b42')
b2sums=('9ace24e952be146f4d44bc492eb5b23fb88d174a5b1ecc85e2a89e2de6ee0a92f00780d9e7b7fc48c5b1120f84dcb980dd8717c43994d6051ad4826b97b31e50')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
