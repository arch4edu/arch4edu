# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=RANN
_pkgver=2.6.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=9
pkgdesc="Fast Nearest Neighbour Search (Wraps ANN Library) Using L2 Metric"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL3)
depends=(
  r
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('9f6b6a8150984b2ae7134d8b0218e35f')
b2sums=('bb3bda1f861f3682a7ad7bfce13001e5f658dbb101dad356ae337fec6ab93cd846c4a1f97c03a2d1c085be47b19bd098691a6cc08cd0c36e8c40dce34c618087')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
