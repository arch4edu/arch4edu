# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <alex.branham@gmail.com>
# Contributor: wagnerflo <florian@wagner-flo.net>

_pkgname=zoo
_pkgver=1.9-0
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
md5sums=('fba440a280e772990f55aeec7257ef85')
b2sums=('c5cc6bffe849a9baf3b997847895b57cc9c0623eb29b841bb4bc37685b4904852a61ef3783553d4cf8fb332582a58790c71aeafcb1002ec000af6a57c7d8184a')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
