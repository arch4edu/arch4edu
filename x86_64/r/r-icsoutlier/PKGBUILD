# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ICSOutlier
_pkgver=0.4-0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Outlier Detection Using Invariant Coordinate Selection"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-ics
  r-moments
  r-mvtnorm
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-icsclust
  r-repplab
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('5f3a2b02876603f8cd642c593295a7bf')
b2sums=('c08a353edc17956674a8d08d793afdd8feb98ae10bd06c6a6c6673a0047d34232734a0463eb2c759c36f120b4c5658e7dcb2297e7a073722d9acf139aeff144f')

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
