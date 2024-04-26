# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=ddalpha
_pkgver=1.3.15
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Depth-Based Classification and Calculation of Data Depth"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r-geometry
  r-rcpp
  r-robustbase
  r-sfsmisc
)
makedepends=(
  gcc-fortran
  r-bh
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('eee5e25fb1559d4aebf0c4343c1214c7')
b2sums=('5e25e4a2cbedbbd82f822a76502862811b2ca2612cc4cff74bf12b0d9972db7b2b4001cd3f3c35aa2063af547d808c23fc4362226a5f0cf31becadde32e029e8')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
