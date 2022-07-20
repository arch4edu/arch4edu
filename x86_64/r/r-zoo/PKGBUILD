# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=zoo
_cranver=1.8-10
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="S3 Infrastructure for Regular and Irregular Time Series (Z's Ordered Observations)"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL)
depends=(r)
optdepends=(
    r-aer
    r-coda
    r-chron
    r-fts
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
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('c9a282d8004c22651c4fa1d657d3cad946c5ec55c4dc068569d860ee9b31ed47')

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"
}
