# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=jmvcore
_pkgver=2.7.7
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
  r-knitr
  r-ragg
  r-rcolorbrewer
  r-rprotobuf
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('df70719f55a52ae6f0d64cd58fa88f98')
b2sums=('4d7f2120a34eb7e0b75783c64dc9dc969899a360b947200f01d0951e3794d493883aff4986bbf72a31c3d52d36d860b79459218ebc403fd85d9a2d79ee6b2f1f')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
