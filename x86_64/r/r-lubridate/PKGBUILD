# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Clint Valentine <valentine.clint@gmail.com>
# Contributor: wagnerflo <florian@wagner-flo.net>

_pkgname=lubridate
_pkgver=1.9.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Make Dealing with Dates a Little Easier"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
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
md5sums=('09977b7de6710ca05886412c6aa3a5a3')
b2sums=('e85b8656eaf4b79f98d5fd6ca74e4c74446d26a68df257ae6f3914e1690b24c27f2f218a58da155cac25555d3d7fe1e738a860841244436fc635d26826329b3e')

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
