# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=DALEX
_pkgver=2.5.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="moDel Agnostic Language for Exploration and eXplanation"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-ggplot2
  r-ibreakdown
  r-ingredients
  r-kernelshap
)
checkdepends=(
  r-caret
  r-gower
  r-kernlab
  r-parsnip
  r-randomforest
  r-ranger
  r-testthat
)
optdepends=(
  r-gower
  r-ranger
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('2248e3ca32208d40b52246cf1a530984')
b2sums=('644174aef32620adf40e587b55046185dc73d64efdb4e94f2234b732aadd85126c1a9458c2c0b389aa583e7e83cb3bdc422cd0a3a2fb74124227d02bc7972c3b')

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
