# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=nanoarrow
_pkgver=0.7.0-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Interface to the 'nanoarrow' 'C' Library"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('Apache')
depends=(
  r
)
checkdepends=(
  r-bit64
  r-blob
  r-hms
  r-testthat
)
optdepends=(
  r-arrow
  r-bit64
  r-blob
  r-dplyr
  r-hms
  r-jsonlite
  r-rlang
  r-testthat
  r-tibble
  r-vctrs
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('3ad14cb4736edde4277b48400dcb1f2d')
b2sums=('d7cb6e43dcc5d9848acfafbb3947aac3732e6f4b0afb7cf38df89e3f88477ee512038032634c64a9abcf5fa65ec67296d8fec07b14cfe5323c0815db15009746')

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
