# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=elliptic
_pkgver=1.4-0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=10
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
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('eb083f4e62ee749a5eec9febb353a49f')
b2sums=('600de80cbb973b99f13a5a378b72ac65c5598e43b33258c7cc8cbd0fd0ec06e439b258adf9c7ad45844213e93aaefd5064fbed4af840366fa3d64f184dd8c102')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
