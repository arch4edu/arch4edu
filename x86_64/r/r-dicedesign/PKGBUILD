# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=DiceDesign
_pkgver=1.10
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Designs of Computer Experiments"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL3)
depends=(
  r
)
optdepends=(
  r-randtoolbox
  r-rgl
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1006a4bae25c296e3ad5a60a62ed719c')
sha256sums=('06543b207b8c1732bda575b9f60ca4ec004f896676e04200af8b222f8933c73d')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
