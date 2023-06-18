# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Matt Frichtl <frichtlm@gmail.com>

_pkgname=Rcpp
_pkgver=1.0.10
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=4
pkgdesc="Seamless R and C++ Integration"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
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
md5sums=('32f9331801336420cae8a04d8c3c9e17')
sha256sums=('1e65e24a9981251ab5fc4f9fd65fe4eab4ba0255be3400a8c5abe20b62b5d546')

prepare() {
  # upstream issue https://github.com/RcppCore/Rcpp/issues/1251
  sed -i 's/-447.1974945/-447.197893678525/' "$_pkgname/inst/tinytest/test_stats.R"
}

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" LC_ALL=C.UTF-8 RunAllRcppTests=yes Rscript --vanilla tinytest.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
