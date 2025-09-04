# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mockery
_pkgver=0.4.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Mocking Library for R"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-testthat
)
optdepends=(
  r-knitr
  r-r6
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('cef9203fa34abb2ec5db83084d92b7d2')
b2sums=('525503dfbaec96189df4913b0db50ed83d74cc4b8b0e1daf15ac2aeaaa977633fa17c9c8ad9a5b6fa2e9bff64f636099e1b9fc68e7b8cf396284e06e09fca662')

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
