# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributorr: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=modeltools
_pkgver=0.2-24
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Tools and Classes for Statistical Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('48310d1e9ac8906a4c9dca16bdfeb27d')
b2sums=('dcfeda90bede43fac69c8a240959d494b4699d4f642e5d02553d985cac0fce2bf44c04be5e89036edb4a80987c395818296a936dae0d709511f3dcb9b6a72175')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
