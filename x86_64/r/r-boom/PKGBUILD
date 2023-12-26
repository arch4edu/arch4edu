# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Boom
_pkgver=0.9.14
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Bayesian Object Oriented Modeling"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('LGPL-2.1-only')
depends=(
  r
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a9d64876d3c5c6e4166a406cc8c16d87')
b2sums=('cb56eb9a516bc68e2b0712d0cefa078c843205e07fce456d593d7618e7f399270552913e85a0162fb6412db03a3ed0b287d3942049b0e9c657fdc1209ccb03aa')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
