# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=kit
_pkgver=0.0.20
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Data Manipulation Functions Implemented in C"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d1060790c5949fcb83eb7ce8c4906517')
b2sums=('71c4188a32c274efe2fce63bbaf51290894de483e60d2f5b1e2133489e50f0f16ef591cb1e9094bd51bd1d65d977e184d7f199ef749528d97ec55b045eec3f4c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
