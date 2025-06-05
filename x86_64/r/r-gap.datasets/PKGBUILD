# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gap.datasets
_pkgver=0.0.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Datasets for 'gap'"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7c698fe9b41dea20f52ee5184f36b269')
b2sums=('76dd98d6df43ee8a4f07ed09d0e88ff6c64c440b0255082df4019eb5215467697b9d6eb4eb6167dce749fcce9237c03f9a7e0a6c267c916981483b8230cfd684')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
