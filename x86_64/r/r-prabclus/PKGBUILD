# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=prabclus
_pkgver=2.3-3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Functions for Clustering and Testing of Presence-Absence, Abundance and Multilocus Genetic Data"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-mclust
)
optdepends=(
  r-bootstrap
  r-mvtnorm
  r-spatialreg
  r-spdep
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a978397e43f43298a994a0c8fcc450c7')
b2sums=('fe4edb65112dfec49f2ce877931d539a93fe478b106e4c45e429de9e850c9f4e4ef064164905b23999c548be5345944b58e8da7db4780904d245423a2b0d74eb')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
