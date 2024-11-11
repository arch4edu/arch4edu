# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=nnls
_pkgver=1.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('1fb723bf426b89950c74c64abba34199')
b2sums=('1a76731c7508d96e7c3c13e66e7a932d3e368d4ceceae8b849056d451a8e5f6a644ed1ddb72f6a7bdbcfb5ea2441ccd65946e03e90d03880f0406b90e2552421')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
