# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ROSE
_pkgver=0.0-4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Random Over-Sampling Examples"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL2)
depends=(
  r
)
optdepends=(
  r-tree
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('73db406449aae225ad8580e309fb433b')
sha256sums=('7750b764f30e2a1cd9bd8768897e83e5e1395f505908fb8923fb76f5e64f7b78')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
