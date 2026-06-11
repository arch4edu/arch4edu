# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ordinal
_pkgver=2025.12-29
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('3cde159a88b96ed9ac797dbe941e00ca')
b2sums=('d6e03f200328ea86fa3d17ae2114ec11beacda62e2774a6d970b7253c018aee19a25cacf6feba64112e4cd9dc621676ac36873cbfd2fced9c744f2b5cd98a00a')

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
