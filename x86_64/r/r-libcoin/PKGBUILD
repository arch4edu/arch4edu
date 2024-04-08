# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=libcoin
_pkgver=1.0-10
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Linear Test Statistics for Permutation Inference"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  lapack
  r-mvtnorm
)
optdepends=(
  r-coin
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('36dbba586a222ba373b5b8bbc61729c4')
b2sums=('43ecb2e4b7a337e81dde4037d4c7d3140bc07c5c9e2cf7da00091cb5c7e3c1133aacba795aa55719f48d193136a4bffec29eea482d60a76ca0ec87fb7cdedb94')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
