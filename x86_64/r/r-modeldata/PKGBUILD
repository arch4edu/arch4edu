# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=modeldata
_pkgver=1.4.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Data Sets Useful for Modeling Examples"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-dplyr
  r-purrr
  r-rlang
  r-tibble
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-covr
  r-ggplot2
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('0f525673d8fb91ad0445d74d4766f16f')
b2sums=('5e31976d7008251dee1285821086bcb095d60113566882d25e3997c722d61c4d92877684e24fd5220f1a433841505460275b4cfc19f93f51b82b7cd1e0b88254')

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

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
