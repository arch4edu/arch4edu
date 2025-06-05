# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=estimatr
_pkgver=1.0.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Fast Estimators for Design-Based Inference"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-formula
  r-generics
  r-rcpp
  r-rlang
)
makedepends=(
  r-rcppeigen
)
checkdepends=(
  r-aer
  r-car
  r-clubsandwich
  r-emmeans
  r-fabricatr
  r-randomizr
  r-sandwich
  r-stargazer
  r-testthat
)
optdepends=(
  r-aer
  r-car
  r-clubsandwich
  r-emmeans
  r-estimability
  r-fabricatr
  r-margins
  r-modelsummary
  r-prediction
  r-randomizr
  r-rcppeigen
  r-sandwich
  r-stargazer
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('2aa81578a1dd27d38e2306998a5f68e3')
b2sums=('f4706a204b3df8699fdc74408943d0aee804e4e4c222320b6d66417660819891c8bb48720c10fdfb96785ca1d786a1d70aac738943b321878ab7f5621726e6f6')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

_check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
