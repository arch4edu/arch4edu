# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=quantreg
_pkgver=6.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Quantile Regression"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  blas
  lapack
  r-matrixmodels
  r-sparsem
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-conquer
  r-formula
  r-interp
  r-logspline
  r-nor1mix
  r-r.rsp
  r-rgl
  r-zoo
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('838f88ce6e3c7ecfb9e2488b2c498495')
b2sums=('4d2eed5a4d500669be80bc101e113f30bca6c881fb90b7be71c039790b9a8044181dfd3eefded922fb20331f0babe2f3e0b7f02e83e51a18c21f85e9521a746d')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
