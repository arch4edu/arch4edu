# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=clock
_pkgver=0.7.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Date-Time Types and Tools"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-cli
  r-lifecycle
  r-rlang
  r-tzdb
  r-vctrs
)
makedepends=(
  r-cpp11
)
checkdepends=(
  r-slider
  r-testthat
)
optdepends=(
  r-covr
  r-knitr
  r-magrittr
  r-pillar
  r-rmarkdown
  r-slider
  r-testthat
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('762d8374cd6998be0c059861f4de8bcb')
b2sums=('35cf1314f21553a3689e4104c43ba9edc78ad4d517082e9880eee99bd5599e87e93afadb684c2a2a8663279ae36e271eb560f2d6cccfab4da18882bf21cb0c38')

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
