# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=randomForest
_pkgver=4.7-1.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Breiman and Cutlers Random Forests for Classification and Regression"
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
md5sums=('31fe6885dccafec29a9315b771c25971')
b2sums=('e5164dae8be0eb14f5f6fca9fbdde065b1479913ec0c1c0f77d7dc0be591efe903df9198c278d9fc99c432052b2f97b8632ea885b720dc4f59c353440d0d63ce')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
