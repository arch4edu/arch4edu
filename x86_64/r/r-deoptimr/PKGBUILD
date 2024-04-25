# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=DEoptimR
_pkgver=1.1-3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Differential Evolution Optimization in Pure R"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('945667c3199760a35837e0a1b72f3648')
b2sums=('56c262a8e48b14ac23098c966bbd6ee4cc85c9f4fc3d89ae190f607f73d71965e8adb682542ebc77a0a243133c111d91dc65fc022d820ba957096844130d209b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" R_PKG_CHECKING_doExtras=true Rscript --vanilla JDEoptim-tst.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
