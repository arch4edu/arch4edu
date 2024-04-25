# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ucminf
_pkgver=1.2.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="General-Purpose Unconstrained Non-Linear Optimization"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  blas
  r
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-numderiv
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('44871c91a7be26117ffad1e685a7b719')
b2sums=('9e857bf94da7980db2ff3b269ae61bec72492b7f36e66fe933da46ef6359d32df4bdcd9e56cdc30304006f197ba9c0cba74779da04e7efe7672b9c85b50d276d')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
