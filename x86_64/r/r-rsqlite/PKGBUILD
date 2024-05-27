# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=RSQLite
_pkgver=2.3.7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="SQLite Interface for R"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('LGPL-2.1-or-later')
depends=(
  r-bit64
  r-blob
  r-dbi
  r-memoise
  r-pkgconfig
  r-rlang
  sqlite
)
makedepends=(
  boost
  r-cpp11
  r-plogr
)
checkdepends=(
  r-dbitest
  r-testthat
)
optdepends=(
  r-callr
  r-dbitest
  r-gert
  r-gh
  r-hms
  r-knitr
  r-magrittr
  r-rmarkdown
  r-rvest
  r-testthat
  r-withr
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "system-libs.patch")
md5sums=('b7dad69abc164564e34ad46a31a8a8c9'
         '29102318ffe7e673c7106be0041c7811')
b2sums=('0aff1be66b5cff2b9c8edd622d4d7f661b5c7868972cecdc32333fc658e8054dd3f1ec84212b73fe668b012bb717506fd19d225748412a8a8990e51e38114b91'
        '8a6c00d199a0a7940c4bca7cd4d162badbdb290c8754552f3a888fd1a6eeabfd2bf8a065d952bae11034071b0a7eb72e39f0786af820ab19908aa9b67bdbfa4f')

prepare() {
  cd "$_pkgname"

  # Skip source code formatting check
  sed -i '/"source code formatting"/a\ \ skip("Do not check code formatting")' \
      tests/testthat/test-astyle.R

  # build against system sqlite and use system boost headers
  patch -Np1 -i ../system-libs.patch
}

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
