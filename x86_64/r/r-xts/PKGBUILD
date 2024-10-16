# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Hyacinthe Cartiaux <hyacinthe.cartiaux@free.fr>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=xts
_pkgver=0.14.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="eXtensible Time Series"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-zoo
)
optdepends=(
  r-chron
  r-timedate
  r-timeseries
  r-tinytest
  r-tseries
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('06716389f3ef7c1468caf67f1191f4b7')
b2sums=('c10212d5869cfa1f5037c721b09d11f7350f9d0b1dc08f48ef6f474b18d884c23e2cb91dfa469ade403b225ffa75f902890380774dc5ace05275a28ffa62538a')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
