# Maintainer: AutoUpdateBot <auto_update_bot@arch4edu.org>

_pkgname=RTMB
_pkgver=2.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="R bindings for TMB"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
  r-rcpp
  r-tmb
)
makedepends=(
  r-rcppeigen
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('2fc174f6d64319b83ce0d12090160c10')
b2sums=('01bc85e8b46a66db2e1ccdd1d7536499817babe1a087f5541badf8d83adb1426ce6f55e9d22fc9b5a0f268410f37e4a58d48ca1a64ede9cad43e3817849a30a0')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
