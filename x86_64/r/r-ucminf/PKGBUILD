# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ucminf
_pkgver=1.2.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('b13fe2db50c37b548ad7355267442540')
b2sums=('9cce2dd1afc449a0b4ce8c5276662b23c3e623000fdc3d1024c9dbe27358f2c4e206ed761eb8ad0a964f38dbb83a63a94f019786879505b42a74e8db4f1b5281')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
