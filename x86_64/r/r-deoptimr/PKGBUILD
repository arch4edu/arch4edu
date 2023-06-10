# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=DEoptimR
_pkgver=1.0-14
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=2
pkgdesc="Differential Evolution Optimization in Pure R"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('57ee44f6058867852035c2f7dc5c8e34')
sha256sums=('d741ddb7bc7243567060c2f00b84f1e3bc709182db9ebd0a9ce94ace2c905134')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" R_PKG_CHECKING_doExtras=true Rscript --vanilla JDEoptim-tst.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
