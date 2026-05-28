# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=dials
_pkgver=1.4.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Tools for Creating Tuning Parameter Values"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-cli
  r-dicedesign
  r-dplyr
  r-glue
  r-hardhat
  r-lifecycle
  r-pillar
  r-purrr
  r-rlang
  r-scales
  r-sfd
  r-tibble
  r-vctrs
  r-withr
)
checkdepends=(
  r-kernlab
  r-testthat
  r-xml2
)
optdepends=(
  r-covr
  r-ggplot2
  r-kernlab
  r-knitr
  r-rmarkdown
  r-testthat
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('fcd2cb48327687e8db4d2c10d92ad23e')
b2sums=('4583521e6071b1a590f01416e0ae32b6cd0f68efa3bccc4b2635ad5800b8260d195f2eb49dea1bc2b320b22793f6eecaab1e0f782ee5688a4562236adb1d2de8')

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
