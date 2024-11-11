# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mda
_pkgver=0.5-5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Mixture and Flexible Discriminant Analysis"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-earth
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('194336329de5d083a8f226d6c97e4526')
b2sums=('64898cc9672bcee1660e71a610ec10ef047e780def074975d03fb93999c3e3a95bb61db2e0ab58d2d6cd55e4130ab9d8fb2f799177993f28b6b3b656381e7fa8')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
