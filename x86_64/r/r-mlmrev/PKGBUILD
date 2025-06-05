# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mlmRev
_pkgver=1.0-8
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Examples from Multilevel Modelling Software Review"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-lme4
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f4d61472c9dd70d0cfc7f31b8a046aa0')
b2sums=('976c2b718444e191b501ef84e1049383c5ccd728cd905469eded1ae74aa5c8eaf9165815faec42ae8090bbf6f953f18a61e817cce922ed3d69ce86e0505b6fc5')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
