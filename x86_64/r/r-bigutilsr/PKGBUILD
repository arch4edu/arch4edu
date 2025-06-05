# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=bigutilsr
_pkgver=0.3.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Utility Functions for Large-scale Data"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-bigassertr
  r-bigparallelr
  r-nabor
  r-rcpp
  r-robustbase
  r-rspectra
)
checkdepends=(
  r-gmedian
  r-mvtnorm
  r-rrcov
  r-testthat
)
optdepends=(
  r-covr
  r-gmedian
  r-mvtnorm
  r-rrcov
  r-spelling
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('49ad25ab76efaab30f5dbaed238f2b31')
b2sums=('def3d1a5c1f5d69016d3569e694df90f531f5b869a0434b83cd7ad9aefc4998196ab9907847db75ed48a218a401f6fc9f241c11518908d928c607df84ec995f8')

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
