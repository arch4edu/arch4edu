# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=iterators
_pkgver=1.0.14
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=11
pkgdesc="Provides Iterator Construct"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(Apache)
depends=(
  r
)
checkdepends=(
  r-runit
)
optdepends=(
  r-foreach
  r-runit
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('e1d875f0ddec6834dd33e56c4f04a706')
sha256sums=('cef3075a0930e1408c764e4da56bbadd4f7d14315809df8f38dd51f80ccc677b')

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
