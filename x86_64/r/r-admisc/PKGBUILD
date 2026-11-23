# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=admisc
_pkgver=0.42
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Adrian Dusa's Miscellaneous"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
optdepends=(
  r-data.table
  r-dplyr
  r-qca
  r-testthat
  r-tibble
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d9031a05b1a8c95e9bf1a2767e7ddc1b')
b2sums=('3fcba836ee8b575950143439876c1b2da7238ef404861e217f072f995966381885e149f16119ed566005158e3dc869e6bf3ce596c7c5cc05c4cd1acd62e942e0')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
