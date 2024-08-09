# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=pcaPP
_pkgver=2.0-4-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Robust PCA by Projection Pursuit"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  blas
  lapack
  r-mvtnorm
)
optdepends=(
  r-robustbase
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('2c14d928bfa8d08166af694c1197a58f')
b2sums=('a56b93322e83df8e7c9d9d10cd236398e64c66594b97ffb16d4d49866bfe43dc73a33572356b8df5df364ff525a88b19d6ab00aae58e73acf53a66585969e280')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
