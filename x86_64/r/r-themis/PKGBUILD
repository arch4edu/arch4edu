# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=themis
_pkgver=1.0.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Extra Recipes Steps for Dealing with Unbalanced Data"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
depends=(
  r-dplyr
  r-generics
  r-glue
  r-gower
  r-hardhat
  r-lifecycle
  r-purrr
  r-rann
  r-recipes
  r-rlang
  r-rose
  r-tibble
  r-vctrs
  r-withr
)
checkdepends=(
  r-dials
  r-modeldata
  r-testthat
)
optdepends=(
  r-covr
  r-dials
  r-ggplot2
  r-modeldata
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8f13545a8a8d475f3323e75dd40a66d3')
sha256sums=('f1350109904c302b1d5ec8ab9d692172a4334a60e252f93241da18d4559fe1e1')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
