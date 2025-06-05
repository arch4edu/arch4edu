# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=faraway
_pkgver=1.0.9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc='Datasets and Functions for Books by Julian Faraway'
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-lme4
)
optdepends=(
  r-leaps
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('ae4b241375f5096e4f50321d94d45d54')
b2sums=('68d006f9611f6ef0ae11e9ddbdd79e9ddc83f2c8d8e335b0fb4793c27e510bba16fb95898990ec2766f7909f88e2b34d38d5808f297837485cdf4871db520987')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
