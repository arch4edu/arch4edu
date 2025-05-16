# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=RSQLite
_pkgver=2.3.11
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
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
_checkdepends=(
  r-dbitest
  r-testthat
)
optdepends=(
  r-callr
  r-cli
  r-dbitest
  r-decor
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
md5sums=('957a787cb20226a5fe52894794e3b294'
         'a4e9a6c34e49e6e36edcf7d46e4841af')
b2sums=('91c2fd93bc3285a3c19d6badc7e13086e4ed9a57d410d40ba5cf35f07ae8059d7b2e8d9f92f1c9b7ae238785db9dd8d7da80beafe38e4eea830b2f61bce182e6'
        '76af4e4ba5f59cd12b616357df87aec8a1906b673b086aac5155a3c0486fddbf8bb7c591f099ce05bbce05e905901d46372a81b01ecd03600fb71df8da0674cd')

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

_check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
