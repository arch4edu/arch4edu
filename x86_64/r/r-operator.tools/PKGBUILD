# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=operator.tools
_pkgver=1.6.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=11
pkgdesc="Utilities for Working with R's Operators"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
optdepends=(
  r-magrittr
  r-operators
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('16c236522901759bd83488e736e406aa')
b2sums=('e2a0f691ac11e0e1a94f3b8ba2fd5da9c9c04fbd802c6c148628630ba86056bad4679ea0b4e6ae3acf08561d3c39872fa0e0ad41d4040d5349b9db25185a780b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
