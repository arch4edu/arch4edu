# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=quantreg
_pkgver=5.97
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
md5sums=('e36187123dc53900e967b3c466a902fc')
b2sums=('492b7d130064264cf8a71d290c202ac34cce0276f2240f8ede5253d0dab7cd670088efe64f77fce029016968cee3d430f8a0d6dc32299ec48b41e539fd0e6245')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
