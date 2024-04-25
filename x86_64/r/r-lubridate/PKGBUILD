# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Clint Valentine <valentine.clint@gmail.com>
# Contributor: wagnerflo <florian@wagner-flo.net>

_pkgname=lubridate
_pkgver=1.9.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Make Dealing with Dates a Little Easier"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
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
b2sums=('bb6e6190f3bca20b61661a64af982431079900ff0a356ebd37de5866aee5dff93f1610a5facd6fe953ceedcce49727c63bcd2abf4bad89ab292478069d8f8508')

prepare() {
  cd "$_pkgname/tests/testthat"
  # skip test that requires a French locale
  sed -i '/"parsing months with dots works in French linux locale"/a\ \ skip("Requires a French locale")' \
      test-parsers.R
  # skip outdated snapshot test
  sed -i '/"vctrs methods have informative errors"/a\ \ skip("Outdated snapshot")' \
      test-vctrs.R
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
