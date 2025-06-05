# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=pls
_pkgver=2.8-5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Partial Least Squares and Principal Component Regression"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
optdepends=(
  r-rmpi
  r-runit
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('ccf58dfc209f2e03d097b5e9ec3e7ef8')
b2sums=('c826e9eecae4c52d91ad687a3bc1792cd8a33669cf4195ab9a906c18284f9c1b05376dab00c29062bb44c767fb4cc518f39b77cddee5341cc15f767e649436ea')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
