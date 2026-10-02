# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=estimatr
_pkgver=2.0.0
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
md5sums=('57f66071f6ba482a6a9c626b48a76113')
b2sums=('dafad8c35d84db1fa01857f4dbec0999a6dedb8d895bc0a71e070da7db8982e3d39ef1d57c07babce9c95eae5ab8d6dfd3b57811bbfc04d4f672a6707b92c4a0')

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
