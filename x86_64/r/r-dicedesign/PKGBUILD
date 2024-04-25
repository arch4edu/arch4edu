# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=DiceDesign
_pkgver=1.10
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Designs of Computer Experiments"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r
)
optdepends=(
  r-randtoolbox
  r-rgl
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1006a4bae25c296e3ad5a60a62ed719c')
b2sums=('6175f768e8a51949471ff81dbad83f527d5c1b2a10730899ec84f5208dc73b42d7f5e584174787c3814566ad2a2291fe7f3d44c3ba0780aee8812f431af20b9f')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
