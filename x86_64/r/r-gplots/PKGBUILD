# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gplots
_pkgver=3.2.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Various R Programming Tools for Plotting Data"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r-catools
  r-gtools
)
optdepends=(
  r-knitr
  r-r2d2
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d7ec5c312dafab19d2beddcf491fd965')
b2sums=('2fc9868c75921ebcdcfe1e214c0facb41af006837d6e95bb7dcd5d5e23896c1bd17e4c99c6951c3c3aa5e2ac83ed2196b2b370555ba57c4f811655feb1c5d206')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
