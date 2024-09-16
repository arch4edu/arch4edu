# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=jmvcore
_pkgver=2.6.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
  r-fastmap
  r-ggplot2
  r-knitr
  r-ragg
  r-rcolorbrewer
  r-rprotobuf
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('bb2cae542ef2206718283ca78a268b07')
b2sums=('99b1684a15b1a42e20e11989aa32a39e9f029cf0d5f962d7db23d02bc71d0bcb7e383abc388588a816c8521c66e67dc4536bb7f88059d8f8d49dcbef25aebf0f')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
