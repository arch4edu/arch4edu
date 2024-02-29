# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=VGAM
_pkgver=1.1-10
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
md5sums=('4775c04874f72d7920d38462f321cdf9')
b2sums=('2666fd04c1a7303dd0d03c6f9de22e963b019ed9217b0f027f64d36b6f111af8763f9bb2821518fbd4035eb293b8747cbb47623abb1ef93e43a1a9e0c9b0709a')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
