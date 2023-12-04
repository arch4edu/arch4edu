# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Jooa <aur at (name) dot xyz>

_pkgname=sp
_pkgver=2.1-2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Classes and Methods for Spatial Data"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
depends=(
  r
)
optdepends=(
  r-deldir
  r-gstat
  r-knitr
  r-raster
  r-rcolorbrewer
  r-rmarkdown
  r-sf
  r-terra
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('b06218c0fc28bc70fafcd40fd60cfd08')
sha256sums=('bfdbb4a62f9fe0c554f88c75af6f214dc9a550da09bd3aefe1115ac6963e0dc5')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
