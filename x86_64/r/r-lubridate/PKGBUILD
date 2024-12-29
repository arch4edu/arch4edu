# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Clint Valentine <valentine.clint@gmail.com>
# Contributor: wagnerflo <florian@wagner-flo.net>

_pkgname=lubridate
_pkgver=1.9.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('ea3efcbcf373e986f6dfb851f720a1a1')
b2sums=('14b92e20daadf64e8ed35432cb9ed42acb72c2f306d2622b73f5f9bd451f52883c81a1d3f9ba5996233c7199ec439e154ad4b939d9bca3d5a7aa96230e915de7')

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
