# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=promises
_pkgver=1.3.2
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
md5sums=('1a2106ac7c685146c6ce5382504260c4')
b2sums=('027bbf74b6e6a1a2dc08183479c4f44d5f2efa8d814d7ed58c6ea1ebecbed7eb08b607b3b31e90354045ab12c7ea2926c573c5639a86e01f6c43adc6e69dd721')

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
