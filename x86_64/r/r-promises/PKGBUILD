# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=promises
_pkgver=1.3.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Abstractions for Promise-Based Asynchronous Programming"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-fastmap
  r-later
  r-magrittr
  r-r6
  r-rcpp
  r-rlang
)
checkdepends=(
  r-future
  r-testthat
)
optdepends=(
  r-future
  r-knitr
  r-purrr
  r-rmarkdown
  r-spelling
  r-testthat
  r-vembedr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1b1184329736b045e11ba2dff81ce6ea')
b2sums=('28c1c66e1ffa72e2ae6f577589a6d413046329aac5c582adf7157c8855b69e80542465c5596d7dbaef6c85eca040b37dead16ddea7495e4c9e0bc01a85c43864')

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
