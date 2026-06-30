# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=pan
_pkgver=2.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('05ade721ed344d4d0c422ce7d07fb662')
b2sums=('b451f1efbd963b63ec6de038535a82145e61efffe3e1458ab2f05f7e491036ad7c1f9460db6a6ce6a2c08ec7521134c080c83d89b0deb53a2cbb08280e8b7c84')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
