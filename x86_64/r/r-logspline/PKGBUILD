# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=logspline
_pkgver=2.1.22
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Routines for Logspline Density Estimation"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('Apache-2.0')
depends=(
  blas
  r
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('bd7d9f2674785722cb89ab2c5894694c')
b2sums=('af6c77d4af12ba77585610762d208303a609797504ae4df9cb7555e4d62fbf0b9033ee4b6617bf6d26f8e90f1e3c64abcebb0a0a0e57a5065b8db52e6980008a')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
