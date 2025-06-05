# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=lars
_pkgver=1.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=9
pkgdesc="Least Angle Regression, Lasso and Forward Stagewise"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f91c3128512aea0b607076f7a46693c6')
b2sums=('d14fc6b4494b5edbf383f5940f05f2459c345a135cf4194545fe2bd219143e68a2381bce56ce4a80eccd0d9488e9be333c0669052e6d8bb8a9b448c53a1dcf09')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
