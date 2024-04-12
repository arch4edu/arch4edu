# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=BoomSpikeSlab
_pkgver=1.2.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="MCMC for Spike and Slab Regression"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('LGPL-2.1-only')
depends=(
  r-boom
)
optdepends=(
  r-igraph
  r-mlbench
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('214eb2fc654fe6e98723c7db7008ec23')
b2sums=('4d501e0410df7e95a59ceb4dcbc0de0f872ffaf569fcadf4a708d706deb2f830226283af8c29abf1393174755a0eb654d4d85273686a30f03e491596a970df28')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
