# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=bdsmatrix
_pkgver=1.3-6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=7
pkgdesc="Routines for Block Diagonal Symmetric Matrices"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=(LGPL2.1)
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4f8ccf979ab7f88fa71b7e45323b219a')
b2sums=('1bceed25e2ab1e3de9d6eb401797d87d4bd7e69bc90c436b41381649b9a1d11e8179fbf6d4ec3d03516c9587cbe7dacb2ecf673e1f10a7afb61bbb46874dd690')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
