# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=SuppDists
_pkgver=1.1-9.8
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('7204ad1a691b0db2d43ce7ded0d40f99')
b2sums=('84558f78e3f69c01fac244cb4e728c13f85c5994d00032b53b43617447703a4d3469568ace392158c4671fa2b27c8492a6dc07ce69d175b5899671228ad7a202')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
