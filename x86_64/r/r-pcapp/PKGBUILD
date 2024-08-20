# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=pcaPP
_pkgver=2.0-5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Robust PCA by Projection Pursuit"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  blas
  lapack
  r-mvtnorm
)
optdepends=(
  r-robustbase
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('95cc41c08f1c0909a6ddc7d9b2429e43')
b2sums=('2e44933f5339351ccbbb6336975a73d65b94757846ca901738173ce929c72e65175fb9f66e0b9ae83d1fc3ae9bf91bcffa88ec7aa84d479f3aabe532a6303e2a')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
