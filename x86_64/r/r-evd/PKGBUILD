# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=evd
_pkgver=2.3-7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Functions for Extreme Value Distributions"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r
)
optdepends=(
  r-interp
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8a5fe3fb5097036c69422cd0848ea841')
b2sums=('6e762331d6bfa6b911a17ed58e9f44c05d6d92899720b9dbf3912b5c8b11266246bb4fcf9e2ea7fef91939f73bcc26ba5bbfea407bb583275fcf3b5b8d9547ff')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
