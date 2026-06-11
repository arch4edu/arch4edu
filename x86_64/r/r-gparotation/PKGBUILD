# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=GPArotation
_pkgver=2026.4-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Gradient Projection Factor Rotation"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('74f7477b7334623765ed86784b913131')
b2sums=('df5ac275d1cf82d101dde01b9f0b6c68369a833dee9d382fd5381ee1ddf8bc9f12fca1c3daa9cd2e52fea2fe5609d7c8079d0dd7f1114fa4f78130efc6895931')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
