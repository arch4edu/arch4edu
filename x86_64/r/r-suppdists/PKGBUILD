# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=SuppDists
_pkgver=1.1-9.7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=10
pkgdesc="Supplementary Distributions"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-rcppziggurat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('2d385b616b980e5187cf5bd8efdbaa4a')
b2sums=('1784969cb99caddddb81142efc401ce50db7be39074ed6b0179b2ef1f51d6d39d8362e96050cbaa37ab66ce2f1f14a06b39c4bdda279a58328688ad9fae96f2c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
