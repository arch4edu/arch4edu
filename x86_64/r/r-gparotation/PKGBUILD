# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=GPArotation
_pkgver=2026.6-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Gradient Projection Factor Rotation"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('2d7ce62be746f5b4a436cc80057a69e4')
b2sums=('aac108da58057940884dd9f7014e77fd7ff20330af4deade3f8352d601c19812d184dea3fc5c3f92b02959a45c88fa027d089b59aa402fddb7e786763cbbc398')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
