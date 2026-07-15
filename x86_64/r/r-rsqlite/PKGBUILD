# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=RSQLite
_pkgver=3.53.3
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
  r-httpuv
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
md5sums=('82267c88d52a98b0a3b988bc63d4fefd'
         'a4e9a6c34e49e6e36edcf7d46e4841af')
b2sums=('219976da99c753fd2b59bf96d856f2ce629f4bf7ef39e420cb96232aa95bff5b180490e7a12111e39f1dddf261415b49dcf1594bd411483efba493a06ee4a1ef'
        '76af4e4ba5f59cd12b616357df87aec8a1906b673b086aac5155a3c0486fddbf8bb7c591f099ce05bbce05e905901d46372a81b01ecd03600fb71df8da0674cd')

prepare() {
  cd "$_pkgname"

  # Skip source code formatting check
  sed -i '/"source code formatting"/a\ \ skip("Do not check code formatting")' \
    tests/testthat/test-astyle.R

  # Link against the system SQLite library
  sed -i \
    's|^PKG_LIBS = vendor/sqlite3/sqlite3\.o$|PKG_LIBS = -lsqlite3|' \
    src/Makevars

  # Use the system SQLite header in the RSQLite source
  sed -i \
    's|^#include "vendor/sqlite3/sqlite3\.h"$|#include <sqlite3.h>|' \
    src/import-file.c

  # Use the system SQLite header in the HTTP extension
  sed -i \
    's|^#include "sqlite3/sqlite3\.h"$|#include <sqlite3.h>|' \
    src/vendor/extensions/http.c
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
