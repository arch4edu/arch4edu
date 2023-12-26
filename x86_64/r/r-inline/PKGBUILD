# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=inline
_pkgver=0.3.19
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=11
pkgdesc="Functions to Inline C, C++, Fortran Function Calls from R"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('LGPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-rcpp
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8416bee4b71797aff118bea35a7c5ac9')
b2sums=('c22ae3641b720c1ac3625377da7dc5a2dbc78d2165571b9e9ad6f3e870197b4a8867bb8f408fc2fa26e726f9a7e993ab4fb5eebfd39b6d9fa6006fe3f8d114bf')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
