# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=dagitty
_pkgver=0.3-4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Graphical Analysis of Structural Causal Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL2)
depends=(
  r-jsonlite
  r-v8
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-base64enc
  r-ccp
  r-fastdummies
  r-igraph
  r-knitr
  r-lavaan
  r-markdown
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('52bd65009157ddfe6d496bc79897c52f')
b2sums=('9fc7136bb6f8c64ccf511138aae46ce7ceee5cc6d8d95a8529240969749381821d093e1c6dfa675d65aa2ace5b5d81934990eb6771a7f29187a27f606628d748')

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
