# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=pbivnorm
_pkgver=0.6.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=12
pkgdesc="Vectorized Bivariate Normal CDF"
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
md5sums=('8b88ddf960b19cb47add2879d9d7f7ef')
b2sums=('97c66eb9a19bb09066e7b4213fe6d16c2462cd67052534d50beae3dcc581cb66daf5eb6c2a4206e178efcd9712dd08177795435670a247e8492a4d5d87e4ca9d')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
