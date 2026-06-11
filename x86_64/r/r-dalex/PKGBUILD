# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=DALEX
_pkgver=2.4.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="moDel Agnostic Language for Exploration and eXplanation"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-ggplot2
  r-ibreakdown
  r-ingredients
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
md5sums=('eb0756c65611440e8d9a11742d47472f')
b2sums=('a53533fca756a05a4748b6eb3698437c7a64c74c35c3b84cd264a8caa0536428796c1799be8db2865e6f80cc35dc873756712bc19fe492250cf8f22267b8b386')

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
