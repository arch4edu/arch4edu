# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=statmod
_pkgver=1.5.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Statistical Modeling"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only OR GPL-3.0-only')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-tweedie
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7cb72ca8992c058178756d623139eb80')
b2sums=('92b20d43961047d5bc6dde6c33300f171da9b0c855f28f8824dde6db7f48eaf46bf7481523b38211d6d504e8f7613f464d7a90967c6129c5cd3ef46f9c38b351')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
