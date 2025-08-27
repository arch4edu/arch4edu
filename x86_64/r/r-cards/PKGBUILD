# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=cards
_pkgver=0.7.0
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
  r-rlang
  r-tidyr
  r-tidyselect
  r-lifecycle
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
md5sums=('3364c4f61981a493181be0fd7eb34753')
b2sums=('3f1c3fb8786e4c7cb2a63519008687ff212ede3efc3ba313adde5220a0c00685c93dd1187a1797bbc66a262f3c2a59acd489af650bef24afe814b6a51b1fa17f')

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
