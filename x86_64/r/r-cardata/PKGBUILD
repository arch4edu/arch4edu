# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>

_pkgname=carData
_pkgver=3.0-5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=13
pkgdesc="Companion to Applied Regression Data Sets"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-car
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('88dc01e1d94d67652d4c4c38d33a8981')
b2sums=('dee8f9b5e73cbb785f445b70b6ae88ca8c7303bc4b361943e937596bcc355374856b64c61b9d325484670c779a6ff6df5a8912ee8f65d3afdbf2b1546f68409a')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
