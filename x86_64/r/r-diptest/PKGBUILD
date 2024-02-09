# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=diptest
_pkgver=0.77-0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Hartigan's Dip Test Statistic for Unimodality - Corrected"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f7229b4ba1ca5ad70d996ce984329d73')
b2sums=('45cca9d159591eec95c19bd4abaf35049d66295c5546f7e21293f7f4566c92a2b3f9f5f68dc91ccabd6471d0fe5c8c6fe74d3cc05235911a82268d3851b0eb5c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
