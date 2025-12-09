# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=nanoarrow
_pkgver=0.7.0-2
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
md5sums=('277e572d146bff95590734abb2ae2edf')
b2sums=('9eadb7eafcc27b59c96a10060371eaf606ec280c5a57b40ce80cfe0366a14c0001311e172825b36350c5b9de028cb474f3c90ef815e6da0d9a4aa2ce98bd06c0')

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
