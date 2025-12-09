# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=numbers
_pkgver=0.9-2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Number-Theoretic Functions"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
optdepends=(
  r-gmp
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8cb779153e80fc808c3f04b3652e14ec')
b2sums=('fc1ffdcea3ad00752ec1ae73fdef13351a8fc997e138b95eddb0b48c832774aeb1bb803db6546a6a17879223df9b1150cd82dd44ce6fb6c6ba9feb5c6408a6f1')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
