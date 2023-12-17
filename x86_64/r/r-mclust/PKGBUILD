# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=mclust
_pkgver=6.0.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Gaussian Mixture Modelling for Model-Based Clustering, Classification, and Density Estimation"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL)
depends=(
  blas
  lapack
  r
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-geometry
  r-knitr
  r-mix
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f26d75021befc4ce52ca46ad3873bd20')
b2sums=('4ca5639bb5e9025ac523cd9d1956c093b6f6924f52db63f7b8f418ae74b0e571aaa7a58c3f82b3a5f9b2d59bd69cb20a60a804fe0149043e6662f1abc36becd2')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
