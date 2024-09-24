# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=prabclus
_pkgver=2.3-4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('742260d82f0fdfe6f8c3da4d72cfd5a2')
b2sums=('f0d44e6d702573a7f63521cc651fd1d60b767835d76dca2facb9df8a5f4554ce2fd51c78c7cd8557e489e346d7f22601faadd31c5bc361e2967c135f34588ad6')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
