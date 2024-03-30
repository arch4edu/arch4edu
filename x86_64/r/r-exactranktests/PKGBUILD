# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=exactRankTests
_pkgver=0.8-35
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=6
pkgdesc="Exact Distributions for Rank and Permutation Tests"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('5c3767db5ff0c9d69b9990d4443f0cad')
b2sums=('513d696cc55e2663ee8f722bc441c5ec5b0f7f9438ccaacd255e09bf40b93315cd6dd33054a433fbd7a3b29a01bac22a252dc956e57522c443763ba71f31c9a7')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
