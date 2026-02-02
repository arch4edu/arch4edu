# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=bigutilsr
_pkgver=0.3.11
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
makedepends=(
  r-rcpparmadillo
  r-rcppeigen
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
md5sums=('64eff2c8c490f17074c00d3c50101d94')
b2sums=('5550070cbaacccb4c89dd9a99b82c78b7a1ea893c8e63e7a23d19aa5ed3e67d4dc80fb1e6509c513e4770586751f1ccb3da3cedba269ae8b0e33bb1518a7effb')

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
