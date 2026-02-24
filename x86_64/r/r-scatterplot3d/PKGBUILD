# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=scatterplot3d
_pkgver=0.3-45
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="3D Scatter Plot"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('05a7a9e977e5a3bde1b1de71d989c24f')
b2sums=('26447e81f473d12396a515afa83dbefb473bd6489ce2f6889f327b11cdf7659681e766fd7e24ace9153c25e1f26486fd6f1068bf0b50671fe900373e20e5efdc')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
