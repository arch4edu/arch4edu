# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=statnet.common
_pkgver=4.13.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Common R Scripts and Utilities Used by the Statnet Project Software"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-coda
)
optdepends=(
  r-covr
  r-rlang
  r-roxygen2
  r-purrr
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('28f6f15ec100a34f9e2b3cc94986b4d7')
b2sums=('099a2056f9348a7f9210078597ac1b2ed2bd5fa09a74e9c05112dfd77b8a725942650092f6ed919bd65dc4ebbfe1533cbe67f5b18809d223d64cb4cc7595408a')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
