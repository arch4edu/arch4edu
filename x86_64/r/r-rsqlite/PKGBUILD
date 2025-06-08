# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=RSQLite
_pkgver=2.4.1
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
md5sums=('88acedaf2b1e5ced3038d0a42b71c2bd'
         'a4e9a6c34e49e6e36edcf7d46e4841af')
b2sums=('3124410842a1d2b9ca7b40fad30fdcd0f338cecc0d86509db5cc5c2f5eb2cec6c11f5c1a6cc535b3ff309ad2f2d5eb71f554d2fb785d17778a8d191b20c41d92'
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
