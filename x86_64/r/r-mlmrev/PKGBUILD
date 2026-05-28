# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mlmRev
_pkgver=1.0-9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Examples from Multilevel Modelling Software Review"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-lme4
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7a4a0e729cb182b6f4477822ddb762c4')
b2sums=('d7215da5f45748f18c42df880557af6d2520cbd10574abe55a0fe63b845478871dc0d0978576d29d707a2c60a01a00e8723fd1c13be71dd8f0a8fa8e44757d52')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
