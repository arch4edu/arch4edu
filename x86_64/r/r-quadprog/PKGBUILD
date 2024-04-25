# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=quadprog
_pkgver=1.5-8
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=11
pkgdesc="Functions to Solve Quadratic Programming Problems"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  blas
  r
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4483c9a4606a3a19da46fa68f02c8486')
b2sums=('42c2d7c9b6a9f886214e15de0e5595b7a72dbd2f47bef29656bb559a36504b964f423a8d33ab3ffd4c4b51e805ff398ef2017af24d461ebcec8fdf9e88624f83')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
