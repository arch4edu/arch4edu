# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Hyacinthe Cartiaux <hyacinthe.cartiaux@free.fr>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=xts
_pkgver=0.14.3
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
md5sums=('c752b13fd32ee2044bc120bffd2b51d7')
b2sums=('fd9840062e289f9069dd9ccb95f8fb7487a957b573c2ac4efd0eff9fa65c9cc25ca5a44883953db5743bfb2da8ba3a49c7b5453e1b6d474198d9dbc4e26ddb5b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
