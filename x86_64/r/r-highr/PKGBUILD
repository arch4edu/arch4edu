# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=highr
_pkgver=0.12
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Syntax Highlighting for R Source Code"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-xfun
)
checkdepends=(
  r-testit
)
optdepends=(
  r-knitr
  r-markdown
  r-testit
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('006fcfa8e16c72ecd1adffdf0cf87e43')
b2sums=('264d5380f4b90ef39efb830cd912ade9b928afd2969824b6eddf69506563d8934c30e291e4ec98baf83f24f084e223ade6f38a9a52ece569475f023d412483ae')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" _R_CHECK_PACKAGE_NAME_=false Rscript --vanilla test-all.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
