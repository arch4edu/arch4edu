# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ordinal
_pkgver=2023.12-4.1
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
md5sums=('ca291ae99575bdcd05cf2f63ff732f54')
b2sums=('4ead24264e3ae5ba4947415e49a55f62b070a02b70a5eda7bdc490f12453e99b43d84b77f1d4992924c2f96433f905beca6ac7423609e0461865e2589a22de60')

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
