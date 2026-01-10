# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Matt Frichtl <frichtlm@gmail.com>

_pkgname=Rcpp
_pkgver=1.1.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Seamless R and C++ Integration"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
checkdepends=(
  r-tinytest
)
optdepends=(
  r-inline
  r-pkgkitten
  r-rbenchmark
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('07b0c414704207cc90bd856771bb0620')
b2sums=('5d70c4c127f267002e19e89b3900f2a306296e4592acbff34fa4f6778d08db8846d7133c865f12801b8bf0ea798c01b6552e83256f0bdfb93aa39ca35d3787f1')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" LC_ALL=C.UTF-8 RunAllRcppTests=yes Rscript --vanilla tinytest.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
