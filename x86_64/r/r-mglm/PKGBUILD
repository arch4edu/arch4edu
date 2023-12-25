# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=MGLM
_pkgver=0.2.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=10
pkgdesc="Multivariate Response Generalized Linear Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL)
depends=(
  r
)
optdepends=(
  r-ggplot2
  r-knitr
  r-plyr
  r-reshape2
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d4c964eaa6fd83920fd9948ade55a0f4')
b2sums=('4900e0585fdc4da3f96839d9f3f9efa9eb101069d5d56531bded5b9636ebb59b9e3dd4c0e1652d56af2ae7950a09c5cbfa7c024dc2261c07c315ebf57383e6ea')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
