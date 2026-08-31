# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=cards
_pkgver=0.9.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Analysis Results Data"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('Apache-2.0')
depends=(
  r-cli
  r-dplyr
  r-glue
  r-lifecycle
  r-pillar
  r-rlang
  r-tibble
  r-tidyr
  r-tidyselect
  r-vctrs
)
checkdepends=(
  r-hms
  r-testthat
)
optdepends=(
  r-testthat
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('9b380b8462d6cd62e030467464528bdd')
b2sums=('e192c7f6504a1d6f67834636e73a47078666ce3b4d67d65df81c04de3a8bfde33287ac797c5e849ffa32f543c990c8b8418f78281e196b80b42af81096e92b90')

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
