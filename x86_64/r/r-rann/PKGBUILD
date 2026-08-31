# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=RANN
_pkgver=2.6.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Fast Nearest Neighbour Search (Wraps ANN Library) Using L2 Metric"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8e96f8f5271fa8941aa23f3adac396d9')
b2sums=('d1e2b5190dae2715ba34fb2cbc78715cef1b789ea7329978946b7db08dbccc3904334e973704076605462d70aac4a9640c7609e84a1e9c7bc1b2ffffed122967')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
