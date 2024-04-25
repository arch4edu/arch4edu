# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <alex.branham@gmail.com>
# Contributor: wagnerflo <florian@wagner-flo.net>

_pkgname=zoo
_pkgver=1.8-12
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="S3 Infrastructure for Regular and Irregular Time Series (Z's Ordered Observations)"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only OR GPL-3.0-only')
depends=(
  r
)
optdepends=(
  r-aer
  r-chron
  r-coda
  r-ggplot2
  r-mondate
  r-scales
  r-stinepack
  r-strucchange
  r-timedate
  r-timeseries
  r-tis
  r-tseries
  r-xts
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('9bf826a22610f5a3f8ebd063404e7183')
b2sums=('ba341e8084edee64d357c6cf6fe774ba7276c14cedc37ff41086ca8245d33991f6b5b238145755eabfc1666cde5ac93b7307c1c429feed90295bbe467a213d29')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
