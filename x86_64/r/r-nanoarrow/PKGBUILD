# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=nanoarrow
_pkgver=0.5.0.1
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
md5sums=('b38e95b7558e866fb8dbb968148c89fe')
b2sums=('b02737dba64fc440c23e2c8ee9b560b08f3f0013fe369c9fb859bcfbc0f520ebd508c72d9d7667c6384c06b69e08318fab8b64cb776f40fbb33398aa9938aefe')

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
