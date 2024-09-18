# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=VGAM
_pkgver=1.1-12
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
md5sums=('4a0711e912466b2821034654ec80c028')
b2sums=('f26e6cfb723d7644c34bb76f2d729c43563730e053170c986205e4c2ab5c8b95d691304c77a9ce5fc058fdedc7ad8d959523dec9914bb6c159600d321c19d74b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
