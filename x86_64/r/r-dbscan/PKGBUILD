# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=dbscan
_pkgver=1.2.4
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
  r-rmarkdown
  r-testthat
  r-tibble
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('bcfcd1fc4b91dca2bff93e9e9c7c59f2')
b2sums=('d7d2878c8738a3c8d845d9ed7a3495588c963bb33317fe788776d35ac8fa33049b3acb6820ca624a8988a9a1a8850bd314f7114e8963498ee6af656328c351e3')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
