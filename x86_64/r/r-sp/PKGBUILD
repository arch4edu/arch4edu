# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Jooa <aur at (name) dot xyz>

_pkgname=sp
_pkgver=2.2-1
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
md5sums=('51a4a22e95cec0c45e1cafaf4ad19808')
b2sums=('1df2a947f850814e00af31aa969c21b6194ecaa3cc8aabf5a1b6872729ac75bfe8a5730c4002a8aa3a7eee596edee5d9118bbe7b8cb3cd483794727512b93446')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
