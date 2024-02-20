# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=conf.design
_pkgver=2.0.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=12
pkgdesc="Construction of factorial designs"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('b2c9aa7afe463356b9af6bb10fd1b2e6')
b2sums=('8565bb16d68f5a9b590d64e42b17e20351d19a9e019b528afaa3b8adbb2651afe16168f70141ea1e66a691cac3840227800b99d0ff6adcc42f0088103721a5b7')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
