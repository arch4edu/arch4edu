# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Clint Valentine <valentine.clint@gmail.com>
# Contributor: wagnerflo <florian@wagner-flo.net>

_pkgname=lubridate
_pkgver=1.9.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Make Dealing with Dates a Little Easier"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
depends=(
  r-generics
  r-timechange
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-covr
  r-knitr
  r-rmarkdown
  r-testthat
  r-vctrs
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('eaa5966c86bf744c2f5d58bbb39cbec3')
sha256sums=('2b6e1406d231b0a14d60b99cc406d159fea5465a5694725ad25343f12cf37fff')

prepare() {
  # skip test that requires a French locale
  sed -i '/"parsing months with dots works in French linux locale"/a\ \ skip("Requires a French locale")' \
      "$_pkgname/tests/testthat/test-parsers.R"
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
