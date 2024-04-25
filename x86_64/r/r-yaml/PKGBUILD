# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=yaml
_pkgver=2.3.8
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Methods to Convert R Data to YAML and Back"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('BSD-3-Clause')
depends=(
  r
)
makedepends=(
  re2c
)
checkdepends=(
  r-runit
)
optdepends=(
  r-runit
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('25606fd9de01159019b5acd8d0410af7')
b2sums=('9dc5d33660dbcaf326fe9239304c7884363f60966a2a60538c59f8281d3de5eb616a05081d74bb85d3b14dc4268c4fb43f5ae0bbda6e5e7e1ff09520fad7a280')

build() {
  # generate implicit tag discovery code
  re2c -o "$_pkgname/src/implicit.c" --no-generation-date "$_pkgname/inst/implicit.re"

  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" Rscript --vanilla RUnit.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
