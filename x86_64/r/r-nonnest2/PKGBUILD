# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=nonnest2
_pkgver=0.5-9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Tests of Non-Nested Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only OR GPL-3.0-only')
depends=(
  r-compquadform
  r-lavaan
  r-mvtnorm
  r-sandwich
)
checkdepends=(
  r-aer
  r-faraway
  r-mlogit
  r-openmx
  r-ordinal
  r-pscl
  r-testthat
)
optdepends=(
  r-aer
  r-faraway
  r-knitr
  r-mirt
  r-mlogit
  r-openmx
  r-ordinal
  r-pscl
  r-rmarkdown
  r-testthat
  r-tidysem
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d73b64d4188c6491a4279d73bfe89de3')
b2sums=('c30b4af68e12772b96555925d52ea5e45040d5ad906e272796aae7505ea57f42c376f709a795d721b21f6f8dcccc3d3e17e525839c8d4b0b3a1f04a1df6ab61d')

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
