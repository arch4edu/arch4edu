# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=qvcalc
_pkgver=1.0.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Quasi Variances for Factor Effects in Statistical Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only OR GPL-3.0-only')
depends=(
  r
)
optdepends=(
  r-relimp
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7267885fb26131f10f8d32d58e8d37e6')
b2sums=('33652ef75b70cab25cd841d1245d7f58cc10c68a5b90da7c6569b077ba7bb295cdb11a4080ca5a00c314229e7a21e439c520ab1dc7c840540ab1c7d81c84282c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
