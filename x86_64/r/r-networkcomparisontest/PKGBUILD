# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=NetworkComparisonTest
_pkgver=2.2.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Statistical Comparison of Two Networks Based on Several Invariance Measures"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r-isingfit
  r-networktools
  r-qgraph
  r-reshape2
)
checkdepends=(
  r-bootnet
  r-isingsampler
  r-testthat
)
optdepends=(
  r-bootnet
  r-isingsampler
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('54319c0e7efbeb201b2c2f29a7ec997f')
b2sums=('c9eaafa5ca2f0135b1a7c15439172e531267a8cdd70be86f3f01e7140daafeda40397f339965ddc6d9802036127202ef098920a7c7efd0dc4fec669e583dcd98')

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
