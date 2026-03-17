# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=libcoin
_pkgver=1.0-12
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Linear Test Statistics for Permutation Inference"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  lapack
  r-mvtnorm
)
optdepends=(
  r-bibtex
  r-coin
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a387c5d0252cba7deb19532f04f999ec')
b2sums=('c1c144e443d0eb454f54d9972ca2d044733ce40df304943e95c7c9c7e0e4635e8a55257d69577e8990fa5383496c149e49849565fe5fb419a41180cb531d889c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
