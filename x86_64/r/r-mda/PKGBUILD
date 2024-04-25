# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mda
_pkgver=0.5-4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Mixture and Flexible Discriminant Analysis"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-earth
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d05782cc524a7c680211bfacdc799ad7')
b2sums=('2ded407127166310c6314a726c922cc95a9bbe5ae3d8eef2492f8485c2eef60da502125ff5893fef7aebeda448bf749ff177349586012e17a5ab75c7ed15e4ba')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
