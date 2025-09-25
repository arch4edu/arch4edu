# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=KMsurv
_pkgver=0.1-6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Datasets from Klein and Moeschberger (1997), Survival Analysis"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('57b2ba5c9ffc5dacd5612c2107e81ee2')
b2sums=('fdb07593c09ec56844f28f378395a4e34b047c10b59254b6b722b88ad68535a46f94e579d3c5cd9f09943e17477d799b9f442cd440a74e2f78a0294aeb166a93')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
