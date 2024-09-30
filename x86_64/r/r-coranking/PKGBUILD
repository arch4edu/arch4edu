# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=coRanking
_pkgver=0.2.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Co-Ranking Matrix"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-rtsne
  r-scatterplot3d
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('e786683ac8e81c0f2c6896f3e24a70a6')
b2sums=('66613bfee1d1aa21939f0e8820c83a8034aae56ad3a2137b687b4fa9ffd4e2851a5b9e3ba45204839289d8d0070504c2584f76c11a7fc0f1008214e2ae9a612a')

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
