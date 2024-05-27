# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=highr
_pkgver=0.11
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
md5sums=('6d32bee4188607bcc5d3676c5cd55197')
b2sums=('5634ac9ecc714480ae858f45f9978b6b2d93f6c0885a95e8ee41c09443b3a0e0cd7f15225f6141f781d0bd1dcf22881db9b1da62fbf45ec809884de9d4ab3b4b')

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
