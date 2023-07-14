# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=doParallel
_pkgver=1.0.17
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=7
pkgdesc="Foreach Parallel Adaptor for the 'parallel' Package"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL2)
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
sha256sums=('b96a25ad105a654d70c7b4ca27290dc9967bc47f4668b2763927a886b178abd7')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" Rscript --vanilla doRUnit.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
