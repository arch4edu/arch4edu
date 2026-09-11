# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=NetworkComparisonTest
_pkgver=2.2.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Statistical Comparison of Two Networks Based on Several Invariance Measures"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r-isingfit
  r-networktools
  r-qgraph
  r-reshape2
)
checkdepends=(
  r-bootnet
  r-isingsampler
  r-testthat
)
optdepends=(
  r-bootnet
  r-isingsampler
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('81dbf71f2d20b2df5b49528c80d1a9a2')
b2sums=('c5471906fbd3483c9764f6b2dfbe84a827214aa7a52b87cf3ba3141103384f54c975c880b3b0adb7b7438df5d0bd9551045b54d7f6dc0c5ce12ef592e6838596')

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
