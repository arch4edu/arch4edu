# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ROSE
_pkgver=0.0-4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Random Over-Sampling Examples"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
optdepends=(
  r-tree
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('73db406449aae225ad8580e309fb433b')
b2sums=('b854cda1c185b1e231974f028d3ef6f7f5df4b3d16ef19b5ee17cf429b60be12544a75b4a8c2c066f1ed67b46b412e1c6bc1b83accbc107db8855a6b6f581ee1')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
