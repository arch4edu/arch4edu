# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=GPArotation
_pkgver=2024.3-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Gradient Projection Factor Rotation"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('bcb6ace2512c0c9a3019e2160a76cf64')
b2sums=('8e13a103c2f5d6350186925bba5d8f7a3a79dcdc011beb8ef7b064c4f31b34c68bc3ca1d9e2962b1f7b35223451d516763bfa0e159aea2d5fedd29280c8e24d9')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
