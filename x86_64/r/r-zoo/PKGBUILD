# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <alex.branham@gmail.com>
# Contributor: wagnerflo <florian@wagner-flo.net>

_pkgname=zoo
_pkgver=1.9-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
  r-knitr
  r-mondate
  r-scales
  r-stinepack
  r-strucchange
  r-timedate
  r-timeseries
  r-tinyplot
  r-tis
  r-tseries
  r-xts
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d948b0cd582fea7c99faa2cdbe5cf305')
b2sums=('6826fb866dce00a8cd19f82f55cef8b6ec7162dad14094cb77e051f9ad347dea1ac74aad6652b2ea03f82245397c80a7778486b556ba0dffa7cfa57208a24d92')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
