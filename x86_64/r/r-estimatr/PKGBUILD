# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=estimatr
_pkgver=2.0.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Fast Estimators for Design-Based Inference"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-formula
  r-generics
  r-rcpp
  r-rlang
  r-tibble
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
  r-declaredesign
  r-dplyr
  r-emmeans
  r-estimability
  r-ivreg
  r-knitr
  r-modelsummary
  r-randomizr
  r-rmarkdown
  r-sandwich
  r-testthat
  r-texreg
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('01c3802204417161962a6557030ec383')
b2sums=('86b13eccfc6885db211a29f7edb3e2f4640d1de847347c033fb237d80632e88b5a5f0ee1520a6909244e70236b55a535ba506daf5f5f021cad7e4da397858956')

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
