# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=tinytest
_pkgver=1.4.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Lightweight and Feature Complete Unit Testing Framework"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a5cd391ceee1425a74e38945a4acc4fd')
b2sums=('0e0c460c067407178e28d745d45834b1a29b439d7a5cb870dedf1c8d6ed7495c6ccc416743352eb798d46ed719d64965ecf4ff12690cacb2c31d8061b5b5d7d4')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" Rscript --vanilla tinytest.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
