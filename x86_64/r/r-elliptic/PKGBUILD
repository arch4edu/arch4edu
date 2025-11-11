# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=elliptic
_pkgver=1.5-1
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
md5sums=('d1b1380dc824401ef4daf83b413d9773')
b2sums=('12e6bd9ad6bbfd6a318eb213ee4e243d17fb4a4b08f1903c8b10a98f927b3fe85490e45e7b037c642501793a1daee396626e608e64ddccfa5c9a4af8cf1a725e')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
