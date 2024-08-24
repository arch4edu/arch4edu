# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gmp
_pkgver=0.7-5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Multiple Precision Arithmetic"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  gmp
  r
)
optdepends=(
  r-rmpfr
  r-round
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('99f5956fe66ea32faa9fcc677ab0ab67')
b2sums=('e14c1861efc73ab6b4511ac80d03a463bf9e4a907bbb3a14065206910158e30f0d29bc92130d2fffc427d7f5e66e1729ca6933ec26d0aaa97f70b77fa7c697d1')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
