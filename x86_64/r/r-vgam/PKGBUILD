# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=VGAM
_pkgver=1.1-11
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Vector Generalized Linear and Additive Models"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-vgamextra
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('84317deb01d6ca4a5f88014200850bf1')
b2sums=('0fc6b65b86ec34fb620a7087b6f5bb0576c0627b8523816e0d43a19cfefb7195b5307983bd8331440c6f8ff576af3d67d8e64445f0cbb80b366b4f996b4c08b1')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
