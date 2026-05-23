# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=bigassertr
_pkgver=0.2.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Assertion and Message Functions"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r
)
optdepends=(
  r-covr
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f455b964406445c3090c6b759455261b')
b2sums=('5a13016910796fe061f3353eaf31ca3eaa3009a74064c47e87c05701d7924fb2ccdf819b8a59c9373adb8f7b8837510d5de589b6df0d7f728467ad99ec8a9ada')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
