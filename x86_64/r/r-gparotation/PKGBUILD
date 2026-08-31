# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=GPArotation
_pkgver=2026.8-2
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
md5sums=('8ecb8f4ba513bdf28395e35bc39f9305')
b2sums=('39cc84b6288216c0ae0bb315ea8b67f71ab8af8d39c3f7aa9303f93fe96f269ed19fbe47f745f28b24e255044eb742afc733926b9998f83ca224f9251e07344d')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
