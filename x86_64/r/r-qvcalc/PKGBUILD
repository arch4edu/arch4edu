# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=qvcalc
_pkgver=1.0.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Quasi Variances for Factor Effects in Statistical Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only OR GPL-3.0-only')
depends=(
  r
)
optdepends=(
  r-relimp
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('2494a818e5a13b2d8b4b7f6c7e3fe8bb')
b2sums=('9f24b01e36aa0c4cbdcc6847a17082aba6ed84e52ce6b8f0290ce2bd5c28ffe4b613f99e3e15c1bf83eb698362d089586d1dc06921f51e5a3fd7c226c9c526be')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
