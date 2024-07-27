# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=yaml
_pkgver=2.3.10
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('f5fad2fbfe3dd8ccb29125fa6361150d')
b2sums=('cfe0cfbf8dacc241551a89828cfbe4e5cce415bac03773244169182024e64acc86796a8d43ffec0b8df7e3e72b6cb946bd97d55688822b9f53b09c676074a96e')

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
