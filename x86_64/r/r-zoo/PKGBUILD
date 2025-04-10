# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <alex.branham@gmail.com>
# Contributor: wagnerflo <florian@wagner-flo.net>

_pkgname=zoo
_pkgver=1.8-14
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
  r-mondate
  r-scales
  r-stinepack
  r-strucchange
  r-timedate
  r-timeseries
  r-tis
  r-tseries
  r-xts
  r-tinyplot
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f3e2b2b808d833e5dc3f236f5e7cb36c')
b2sums=('a3963f2d2a66df3ba180f5a96d83b4efa8b4cbc1cd37fea524babc8e05706a8fb2f9deee9d5339af0dd509a4c707264f4b2512885ff4562ed55e27bcd1ce1961')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
