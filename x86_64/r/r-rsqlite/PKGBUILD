# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=RSQLite
_pkgver=2.3.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="SQLite Interface for R"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(LGPL)
depends=(
  r-bit64
  r-blob
  r-dbi
  r-memoise
  r-pkgconfig
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
  r-rlang
  r-rmarkdown
  r-rvest
  r-testthat
  r-withr
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "system-libs.patch")
md5sums=('7ae283a80ebc2203e6b6831dfc199fe8'
         '29102318ffe7e673c7106be0041c7811')
sha256sums=('32b1d0ca464da2b61c1e7a11e979c35516a954ee94352285d9f451c630942c44'
            '744c6d1ba721cc0dcde85d0e861257bc3687aa066764c3b898750b3436799084')

prepare() {
  cd "$_pkgname"

  # Skip source code formatting check
  sed -i '/"source code formatting"/a\ \ skip("Do not check code formatting")' \
      tests/testthat/test-astyle.R

  # build against system sqlite and use system boost headers
  patch -Np1 -i ../system-libs.patch
}

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
