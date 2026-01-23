# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gbm
_pkgver=2.2.3
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
md5sums=('044b67e73e2d0231434b8ef9dbc9366f')
b2sums=('5eaae8fb9292f0ed5c4ade4fcc1bdf8c8fda4bafce126a9bcf7c8594b6d27fa3125363c70c5766feb050debca6724de8e5e88ebd55d296b12b1c51f55c8b2ec0')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
