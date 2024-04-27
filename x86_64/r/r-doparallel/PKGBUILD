# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=doParallel
_pkgver=1.0.17
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=9
pkgdesc="Foreach Parallel Adaptor for the 'parallel' Package"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r-foreach
  r-iterators
)
checkdepends=(
  r-caret
  r-mlbench
  r-runit
)
optdepends=(
  r-caret
  r-mlbench
  r-runit
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('df72884b8d87b06c6bdd4f8caf7e5bf7')
b2sums=('451e78bf63c641fbe0a43a4fac2f3c7ad646109a1c24294c3db56fb421efde9a42dea64556d3504ed335d50f6b6b00ca5abeb4485caab5643a291f44c4b44b6d')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" Rscript --vanilla doRUnit.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
