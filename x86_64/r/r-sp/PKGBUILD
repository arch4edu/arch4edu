# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Jooa <aur at (name) dot xyz>

_pkgname=sp
_pkgver=2.2-0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Classes and Methods for Spatial Data"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-deldir
  r-gstat
  r-knitr
  r-maps
  r-mapview
  r-raster
  r-rcolorbrewer
  r-rmarkdown
  r-sf
  r-terra
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('98e65470f5d8d71f2d4f12bda29b1608')
b2sums=('25a307690a3af3380bdd86026b56164f9d458b24e8f2a7da7dec6de8c311303f04c815fee90f4ed2a120908be806cbefcb0393ccca1f546afca77201ad08e966')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
