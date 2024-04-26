# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=shinyjs
_pkgver=2.1.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=8
pkgdesc="Easily Improve the User Experience of Your Shiny Apps in Seconds"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-digest
  r-jsonlite
  r-shiny
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-htmltools
  r-knitr
  r-rmarkdown
  r-shinyace
  r-shinydisconnect
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('23479086c139ba2d7d00c557f1e8895d')
b2sums=('28df9b7c0e4b0b8f958703fabedb99feaccda72302e8fe5250f588cd9a64b48efbb5b77abcd62424d519fff033d01a82d82c03801f0d9ad1cd4be62864af090a')

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
