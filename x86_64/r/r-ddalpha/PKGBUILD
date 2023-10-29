# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=ddalpha
_pkgver=1.3.13
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Depth-Based Classification and Calculation of Data Depth"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL2)
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
md5sums=('60c444f7f82ed56607c87df9c7caec05')
sha256sums=('e4a60a4e0950a3587db2a2d5958ab4fbe07b2548f7c3d4795912fe45c77a4eae')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
