# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ordinal
_pkgver=2023.12-4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('a14e655e739d633b0d4e19220509f638')
sha256sums=('f5582ad983dfd2ffbaf1e90b49af6f2cc319953d1fcb33f31c6c6f335cbd9fa2')

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
