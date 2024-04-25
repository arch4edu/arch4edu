# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=rjson
_pkgver=0.2.21
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=12
pkgdesc="JSON for R"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1670add2df4997c5ea615a6803d356a3')
b2sums=('f9bccabb8beab62d3dd6331bacb2a2ad40af38c459ee73b71592f5904b809685682566d2d606d98cd9b7f3a6e1f47b1e252e565827b1836460041e8fc228c45c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
