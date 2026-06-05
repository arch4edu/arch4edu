# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=libcoin
_pkgver=1.0-13
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Linear Test Statistics for Permutation Inference"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  lapack
  r-mvtnorm
)
optdepends=(
  r-bibtex
  r-coin
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('0b06f2e2cfc30448179ace1b1a770c11')
b2sums=('c0d69ed37a25c7f8b76202be91c2301ce446025efa3eb9282c45b99adfa077294560ed52fbbd2bddc5a1d97e8a98e5f23dc58145a2bc6a3eee209be3646e7881')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
