# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Matt Frichtl <frichtlm@gmail.com>

_pkgname=Rcpp
_pkgver=1.0.12
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "fix-version.patch")
md5sums=('85d8f0c330b934bc8f498be40185a315'
         '50440aea988c07da6fbcfc6ad945679e')
b2sums=('511f3071d81531cdbb6de9b633e1406bb865a462587ea1e0e36c9d760cd9ea80a4ae67b44f2e2b7b5861fde727c0324bf9c3ea2b3cb9085f829fb1cb8dcd88c5'
        'a11024a357cfda063cd3599290ba58f749b8107d888407ec333f1cd2558ba6cdd07a24e7d61aff74d176e31b9470b475e5e86c682b71637e2bea9776b714835d')

prepare() {
  # fix version definition https://github.com/RcppCore/Rcpp/issues/1294
  patch -Np1 -i fix-version.patch
}

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
