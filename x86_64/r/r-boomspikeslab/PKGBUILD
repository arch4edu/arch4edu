# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=BoomSpikeSlab
_pkgver=1.2.7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('e97c76a79079403f8d01ccbfe465fa96')
b2sums=('ef1b661b67a5f4acbfa94af860592bdafc1ed5f136893b256afb97ae579f14c2076e617ef84f3d92a642f890b73d1c006f7f23b24d0a027a90233f2a0c02cc31')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
