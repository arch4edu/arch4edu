# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gbm
_pkgver=2.1.8.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=6
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
md5sums=('55746a84b439a943e9a39149dd371825')
b2sums=('5a075659056e1b4c0e7c0017265e9b2e16941c8f60a7830515cd5dd42728643f55d80847c812eadaa3a47e0b67a0b5c4d6677f9d86fe6c51bb6346b27814070b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
