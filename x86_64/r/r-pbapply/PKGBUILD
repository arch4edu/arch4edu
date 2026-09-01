# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=pbapply
_pkgver=1.7-5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Adding Progress Bar to '*apply' Functions"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-future
  r-future.apply
  r-shiny
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('5a7e1d9183bf7dd782d3c96539314717')
b2sums=('00b940cc38b3ead5fa8bb73036ab14edffce59f465bd41dd22542bad133c9c2fc22b4c4007d1db12fd6260f67cceee924e5226cf9c7302149cac25c346b46c72')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
