# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=quantreg
_pkgver=5.98
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
md5sums=('842e99be00d66ba8c41178a102bd2312')
b2sums=('c300b2c9373bdf23ab4832cfdeec17b7680f8aec8fd19df4e3e52bef4c657d4ec9c9a0cf819e9f3e86221c29bd065b1db85a0f9de897f1c0f11a8c122e0d7f63')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
