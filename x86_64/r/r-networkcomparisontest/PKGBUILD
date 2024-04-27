# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=NetworkComparisonTest
_pkgver=2.2.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
md5sums=('c699e7be5bafd726a02a5721f625b4cc')
b2sums=('9fbcb67264f5b61e5a569aae248ffe3b1ed9f30b704d9b9d4a38458a476e6d761dbe6d17b39faf57fe461cfc0fbacac7bca10ee84cbd59de36af28bb6219e1c4')

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
