# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=randomForest
_pkgver=4.7-1.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=10
pkgdesc="Breiman and Cutler's Random Forests for Classification and Regression"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-rcolorbrewer
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('605493f557b7ba08151062e7d1a63495')
b2sums=('5c67beec88ab6cd6166d6044501f1ecb67edb0d04892b7af61b82d0834d4b604bed406c6d6d243580c2588754a1a42801dddfb25182b6a59ce7ca14f4d9aacad')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
