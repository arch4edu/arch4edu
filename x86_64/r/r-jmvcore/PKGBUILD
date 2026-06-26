# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=jmvcore
_pkgver=2.7.35
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Dependencies for the 'jamovi' Framework"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-base64enc
  r-jsonlite
  r-r6
  r-rlang
)
optdepends=(
  r-export
  r-fastmap
  r-ggplot2
  r-jmvreadwrite
  r-knitr
  r-ragg
  r-rcolorbrewer
  r-rprotobuf
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('e9be33a142748deba034ad7819145d5e')
b2sums=('e4de62555684f1ee30e44721aa24aa35db124c99b1ae6c559c05b41419c1da3534e79efe0b1fc44ae327543fd9e9785d3c4989f166e3243e7a751a39fdea7670')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
