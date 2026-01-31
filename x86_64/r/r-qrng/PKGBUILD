# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=qrng
_pkgver=0.0-11
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="(Randomized) Quasi-Random Number Generators"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only OR GPL-3.0-only')
depends=(
  r
)
optdepends=(
  r-copula
  r-randtoolbox
  r-spacefillr
  r-simsalapar
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4f388d7dcceb3eed9a06a8904e898853')
b2sums=('8f735735a07d6f325f00532e186067d8e705bc2e0fa0a9096a268e3ed1f72b1d6c49c50b68d9658de525fe854deaef09a5f516798b55f308c0e1ffcf54f4860a')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
