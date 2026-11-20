# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=dbscan
_pkgver=1.3.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Density-Based Spatial Clustering of Applications with Noise (DBSCAN) and Related Algorithms"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r-generics
  r-rcpp
)
optdepends=(
  r-dendextend
  r-fpc
  r-igraph
  r-knitr
  r-microbenchmark
  r-reticulate
  r-rmarkdown
  r-testthat
  r-tibble
  r-tidyverse
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('39fc873c7e75da327c4a1a75e52d6ae2')
b2sums=('26c7f34c68bb091e4386f680e3e079395a33d5a88a572bdb9dd541ec8a576873785e1969854a4788a7c2fe318ea1690835839d8137c7d3709b53698e562c0b31')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
