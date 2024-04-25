# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ordinal
_pkgver=2023.12-4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Regression Models for Ordinal Data"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
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
md5sums=('a14e655e739d633b0d4e19220509f638')
b2sums=('622114d4acd1c44e0d2f41d53d7832e9364b3acb5431c719887d80e56b32638dc146c277badca314c930a32a534a20fc4cc3f397d0b8bca76305a1aa69f7e742')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla test-all.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
