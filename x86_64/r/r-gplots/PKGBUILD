# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gplots
_pkgver=3.1.3.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Various R Programming Tools for Plotting Data"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r-catools
  r-gtools
)
optdepends=(
  r-knitr
  r-r2d2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4dd687c541fb88500ea28d9f4161f0b6')
b2sums=('1fc4a561d037449a0c420d34749108761bfc27e4c88ae5b964db0163726b4c0b274dd7754e2038b32f7cd677a072db913bccc2b366bfb1b475e1268796e6c513')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
