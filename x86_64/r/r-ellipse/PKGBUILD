# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ellipse
_pkgver=0.5.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Functions for Drawing Ellipses and Ellipse-Like Confidence Regions"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('ebe98db0904bf2228bdc8c79ac19c665')
b2sums=('9298409c12c4e01901d8bcd5dddafdb0c6d3f1f84771d34a1eb87acb98dbeb9277593c6d2754164d87a2f612d02a6de94a2225e9ad84901aa0769d79b83bbaaf')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
