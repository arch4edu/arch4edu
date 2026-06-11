# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=polycor
_pkgver=0.8-2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Polychoric and Polyserial Correlations"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-admisc
  r-mvtnorm
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('6d60686d03d2c73c663d37c0829a3d9d')
b2sums=('9bf8c364fdbd6ccba5b1c5b0fee4abb74d30fabfc358e2f37aa86cc53dd8e95344e687aeaa96948e27240db3afb52da2d375a0226944c9c7bb3a03dcefac74ca')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
