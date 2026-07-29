# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=muhaz
_pkgver=1.2.6.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Hazard Function Estimation in Survival Analysis"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('507ca4e70109075d9a871b1a7facbeaa')
b2sums=('4183c007812ea77c557b26d38ba8958fd7bc206ebdea0f22561a4be142fa3d64927dd916e76a5eecce8235cff7d78f0972eea9b175cd868b36b12856b9a7b737')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
