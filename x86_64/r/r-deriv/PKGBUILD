# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=Deriv
_pkgver=4.3.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Symbolic Differentiation"
arch=('x86_64')
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r-rcpp
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('c4ab30c4b69b3f42122d6eeb2b3e3469')
b2sums=('1d2e11969f432dcbc021226334fc81f346f3e2e9c1640a6d0390339d67d8ab66b6328c62965d7348f27eb684f4767fbd0cc385d5c65cb612ebc3dc6006596816')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
