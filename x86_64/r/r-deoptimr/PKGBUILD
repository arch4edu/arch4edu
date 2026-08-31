# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=DEoptimR
_pkgver=1.2-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Differential Evolution Optimization in Pure R"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-mirai
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('5d16e94ad9e17e836a3155305594951e')
b2sums=('181e9b22ccbbac83fedb8eaef80d196f4880b9fec4a6cd44f5400d80f78def0cdbf701b51259ed065da4f09654c5a87e97aa0f820f551a5a4409ab08f165122f')

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
