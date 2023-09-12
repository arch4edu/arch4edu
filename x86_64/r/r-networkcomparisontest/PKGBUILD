# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=NetworkComparisonTest
_pkgver=2.2.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Statistical Comparison of Two Networks Based on Several Invariance Measures"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL2)
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
sha256sums=('11f61db9031c54ed28dce0310f51270b0bbd60bbdbf0ec565beb79a80f4e6223')

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
