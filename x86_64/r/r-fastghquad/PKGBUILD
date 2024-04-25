# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=fastGHQuad
_pkgver=1.0.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Fast 'Rcpp' Implementation of Gauss-Hermite Quadrature"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  lapack
  r-rcpp
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('168efbf133355e63193f849fb2ca4342')
b2sums=('7efd003cf24999eb5dcc910524a156826a9316603a6e1323ec1551d41131fc4bdc4c090381f53ae22cfd5fdbd0739651af669aebff509e1729903d7e8f5145c9')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
