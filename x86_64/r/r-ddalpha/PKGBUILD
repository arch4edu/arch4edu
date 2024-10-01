# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=ddalpha
_pkgver=1.3.16
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('a533869dcd5a23ae29af063de13200af')
b2sums=('c8c4fc4d5a32f29a644274b0964bb14e85d4e1c35ee6750e16370098650ad2c98cebb8673ce817ab873aec131c874ac373c6807b7997c6a1d38b9baad0d9b2be')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
