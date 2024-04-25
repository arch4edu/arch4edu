# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=tinytest
_pkgver=1.4.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Lightweight and Feature Complete Unit Testing Framework"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('e8d57668032bedd980cc9f1ad9c957d3')
b2sums=('7ff48d2c8ea5c96ca52dfcc7c17c05b9fcc59b23afaf5dd8a79b8d04b747960481c1ecce26e26380756a0066ea799a29a9adb59f878013e862d8d74702e1f19a')

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
