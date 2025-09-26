# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=elliptic
_pkgver=1.5-0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Weierstrass and Jacobi Elliptic Functions"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  pari
  r
)
optdepends=(
  r-calibrator
  r-emulator
  r-testthat
  r-hypergeo
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('e8c90b9a661aa7f39a7d81a779286db7')
b2sums=('7634eca3d64e165850bbd1488b9ea4d498d43aa59cabf3d4c233f3a2aa138fb0df99f5aab8e7f1e051d9cee4466f39ee751342367faa1cd8aa96cbf01fb933ec')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
