# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=nanoarrow
_pkgver=0.6.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Interface to the 'nanoarrow' 'C' Library"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=(Apache)
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
  r-hms
  r-jsonlite
  r-rlang
  r-testthat
  r-tibble
  r-vctrs
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('60863f348efb6f876a139da5adec52ab')
b2sums=('db2629689ff96406a51619a0c13a6c8875697c7657edf4ada28ea6cb9e3d43259547d3f1d8a110c70ddbbf7f07996d0860d9b5c675409d6f3207a612d9fc2ef4')

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
