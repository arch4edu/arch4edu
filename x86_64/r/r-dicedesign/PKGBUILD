# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=DiceDesign
_pkgver=1.9
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
md5sums=('559d62babcbefb75bef9bb872e4ab0d3')
sha256sums=('93c23730e02471e4225f0254f47d838b5e113162316e3640cccebf5e8cea11a9')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
