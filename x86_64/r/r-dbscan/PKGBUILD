# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=dbscan
_pkgver=1.2-0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Density-Based Spatial Clustering of Applications with Noise (DBSCAN) and Related Algorithms"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
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
  r-rlang
  r-rmarkdown
  r-testthat
  r-tibble
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('e2a15dff636a55a4abc3a65b3978d31a')
b2sums=('5f24a8fdc27c98ae3584c04d8a28a2bbc89084fee60b5d1db770e5f80f4ab60f4367dbc7d2c0642728f0c504c3361fae108bad12f819508776e6ea2663fe9c8d')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
