# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=RSQLite
_pkgver=2.4.4
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
md5sums=('5f57d61e1772b91a429c3db5b26875f3'
         'a4e9a6c34e49e6e36edcf7d46e4841af')
b2sums=('f2c5b054740b01745266a89cfab4be79a2487a64e32ae7f255b4c159a7f68816f0a9b2621d311954404712dad9d95cac79c85b93b7861aaeaaf360cbc9bc2180'
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
