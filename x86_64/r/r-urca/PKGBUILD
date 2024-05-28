# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=urca
_pkgver=1.3-4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Unit Root and Cointegration Tests for Time Series Data"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('9bcc2ab304c406a66f494f34a02ed1d7')
b2sums=('fe39787862791fcf8ba048b399fc28374af7d371c51f9bf851b01f08b01060f74c20f7d8f1acff74ce66616bce291ac8839ff47d389da5fb3a9c66fba175c524')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
