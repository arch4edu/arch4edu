# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ppcor
_pkgver=1.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=9
pkgdesc="Partial and Semi-Partial (Part) Correlation"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1b9b87359c7b491cfc5e4acdb2b2125a')
b2sums=('bfcbaeb71131fa68c5f7da01aa856a20d339384fd22337587ebb9029eb9d9e656c8eba7b373dcccc58fb25e3c88699e64ad341fd5dc0357e5f1dd64fc13a0e7e')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
