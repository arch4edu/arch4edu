# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=GPArotation
_pkgver=2026.7-1
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
md5sums=('ecabbfeefb676bff2e995f6726d12d9b')
b2sums=('8bd9e45840073fd9f5324e6137f1da7ae57f3ca7b2a0f9701eeeabe86abb62f7b47800847f7c6aee01686d17828a9404e20080c6873d817d10d299a6deb74875')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
