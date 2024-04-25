# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=nnls
_pkgver=1.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=5
pkgdesc="The Lawson-Hanson Algorithm for Non-Negative Least Squares (NNLS)"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-bvls
  r-quadprog
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f1aaeef79fbbd3aee167b19b3f512e27')
b2sums=('6696f86729404e9187923a6b6ce2e2e26103024ffa289d84a0162113b6994746a5d7f0d9cbbc4ce6971b596753b07b20eb6d21bd4bad5ef4bf0e216b5e3be855')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
