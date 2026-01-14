# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=prabclus
_pkgver=2.3-5
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
md5sums=('74e9b35d4ebc232718f5741cfbe8a9a7')
b2sums=('3b2e62481a5b83a29513ad78fbc3c9fc484cd0401f9a71ab0cdd2265d06dd79e316b9ba4de6a2c210acb95ac402774bd2c14a6466cc5bc1d4fe3cba6a6f2444c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
