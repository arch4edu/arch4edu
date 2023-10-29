# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ordinal
_pkgver=2022.11-16
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Regression Models for Ordinal Data"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
depends=(
  r-numderiv
  r-ucminf
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-lme4
  r-testthat
  r-xtable
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('66cc1aa18294ae6295d237b92e111817')
sha256sums=('5488ad1dfa531a09d017d68d7393d376c8bc49cceeaa6a3e5f7d57b99168d493')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla test-all.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
