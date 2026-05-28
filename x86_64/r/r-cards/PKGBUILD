# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=cards
_pkgver=0.8.0
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
md5sums=('47ea5546b7ff5b8078ea2fb76fae67a9')
b2sums=('e755a6ce75e322f366837801697e2ab63cbe9afd414e4d0b37fdab1ca487e47c335377d645a0f5db5d29f82b7736f1f93ac22756904dc2a483a924cd2675d71e')

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
