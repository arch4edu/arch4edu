# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=gsignal
_pkgver=0.3-7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Signal Processing"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-pracma
  r-rcpp
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-covr
  r-ggplot2
  r-gridextra
  r-knitr
  r-microbenchmark
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('95c7f3421559c6a1cca4026d378ffdcc')
b2sums=('801e41b7186e448b7348af2233fd8024c527b0ab281d5f7ba998dac7ccae754a0649843bf6ad6078ee6531d263eb7c889579c77bb3d0a63b88c2f828a938d6d7')

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
}
