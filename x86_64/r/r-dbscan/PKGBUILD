# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=dbscan
_pkgver=1.2.6
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
md5sums=('edb50e67fba7fc8c731be69e4f694978')
b2sums=('13d5f283c4f1e7e2413527c53be3ad79c88fc939f22d59c729d5a02f7de31a594cea03f02431ebf924016497480259f1249e7e0392a46589c0ce2273fa2bbf68')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
