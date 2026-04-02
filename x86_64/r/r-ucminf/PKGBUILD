# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ucminf
_pkgver=1.2.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="General-Purpose Unconstrained Non-Linear Optimization"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  blas
  r
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-numderiv
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('fd18b6d10604083577a31da32b5e13f5')
b2sums=('18d5f74d7bab27c9164d9a173855fd47ce112e98093518b695de90f17bbfd71a7fa456899d292bc60aa9fe9204faf2afb589aa995cc4cfed3f4f04d8966feb6b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
