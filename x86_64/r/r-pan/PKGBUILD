# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=pan
_pkgver=1.9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Multiple Imputation for Multivariate Panel or Clustered Data"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-lme4
  r-mitools
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('b6c1c18a3f9b89f068878e065b1f00a4')
b2sums=('11d9cb7bee2c636c8a1bdb389c09b44b9ea22a3816df7024bf910cd61316dbc84cd1196756e4d6e5e54ec28dc1c5d044946f987f9325206de4c783c1e2a1639e')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
