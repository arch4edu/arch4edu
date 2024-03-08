# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=logspline
_pkgver=2.1.21
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
md5sums=('58281b79aef9dfb57e8e6a36effeb71a')
b2sums=('96235b760a5885d1d963a23a6a05bf97a60be7ca2d20f483295480cd63b8b928877a7478e857019c85df8f259155a9bacb4e14958a49db812c0e9aafa6fa60a0')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
