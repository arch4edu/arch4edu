# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=nanoarrow
_pkgver=0.4.0.1
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
  r-rlang
  r-testthat
  r-tibble
  r-vctrs
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('9c1037cd5d73738287a363799e3c23ea')
b2sums=('9bd25a6bc79e9bd5c54047f8130ed86dfc2df398b62c66a43c19cb45b545171840f9ea665bdffee4765292232bbd1017474634ae465ca3626032327406449a21')

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
