# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=exactRankTests
_pkgver=0.8-36
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Exact Distributions for Rank and Permutation Tests"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('3a31d74c38dda248bab9d5725286cddb')
b2sums=('08391486f04fbbe265856e4701d407afd0abfbaf0713b9994bd643412a0ad2d7d67cfc541558e83d00e0d884e5e861b9277bf9340f73ce36fa3ce9a97c0fdf47')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
