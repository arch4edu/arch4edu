# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=themis
_pkgver=1.0.1
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
md5sums=('d88baad98cbabe3c7fea5ace64d1fd8f')
sha256sums=('01bde2f10dacc435685a8df19aa4992e71d099c67e239faa9baa45da15c3d056')

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
