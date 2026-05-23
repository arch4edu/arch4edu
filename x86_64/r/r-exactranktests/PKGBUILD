# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=exactRankTests
_pkgver=0.8-37
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Exact Distributions for Rank and Permutation Tests"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('6d9c70d1db292600dc2f227128742ea1')
b2sums=('1012199541adcf3def02f3af340fafa8b55cae99713dfbe663ac908a1195d80a4d18458fce4a200a9f065351962704945bd571499316a4933f4089d2958e9985')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
