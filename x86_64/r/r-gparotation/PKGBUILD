# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=GPArotation
_pkgver=2025.3-1
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
md5sums=('102cdc5a671bfca1380b6f9c6a9d4fb7')
b2sums=('b7fd4faa1d9eacb9ac296e4f754a097ea2cd7c43352db7f065d918a7fdfec2891a1c5e715c174c25ca3d915b0045616eee6e2ba67f1ad8b7eab4934538ee6b04')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
