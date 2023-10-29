# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mda
_pkgver=0.5-4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Mixture and Flexible Discriminant Analysis"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL2)
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
sha256sums=('f25f7f28807d0fa478b1b55eb9d026ebc30577d9d5ff288f9abfe1f3fdb8a759')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
