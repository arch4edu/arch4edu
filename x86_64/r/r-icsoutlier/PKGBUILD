# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ICSOutlier
_pkgver=0.4-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('5251c1f61b6921346df376852c66ad92')
b2sums=('fb1749c5194fbc71cd451d7c6cd2b99a9b5e2306f1da864b72e01f7e93fdc070e53eef1cd3e73dd49778963179e1c62a64730a6a5e2971185cb8ee8badf1eced')

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
