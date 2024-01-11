# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gbm
_pkgver=2.1.9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Generalized Boosted Regression Models"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-covr
  r-gridextra
  r-knitr
  r-pdp
  r-runit
  r-tinytest
  r-vip
  r-viridis
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('5c4da29542ad19ad41d0d6685d7c75c9')
b2sums=('34c8110371d5c6b7cd9752a791d721d93f374a080773311b7fb1abeb85c46ed0622aabbdec82ec4c31e1986c1cf61c0d3e9a04fbb8fe702887abaf8db6801cb4')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
