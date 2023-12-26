# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=matrixcalc
_pkgver=1.0-6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Collection of Functions for Matrix Calculations"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL)
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('3b7acd84cfbe8085fab05d2f40ff0c79')
b2sums=('b9f4a3af74abf04c32bf9a3acaafa23cc6ea42fd45e79add4213c909501adaff4331947eeb925c1eec6f142d5dd8e75e92e675430de5ac6d793356e9a1df36c8')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
