# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=sets
_pkgver=1.0-25
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Generalized Sets, Customizable Sets and Intervals"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
optdepends=(
  r-proxy
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a312dd5cf3d7df308781508d57c298b0')
b2sums=('f8c05f6a3bc09b9259520e1985799ccc12d16aff4477db3a5ddbf3f0264bd31902e06e630515cff36c271f0bf7c354706debf69ef3ff560b1f0adc78f22c48f1')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
