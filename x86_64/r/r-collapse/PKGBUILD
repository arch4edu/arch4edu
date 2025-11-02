# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=collapse
_pkgver=2.1.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Advanced and Fast Data Transformation"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later AND MPL-2.0')
depends=(
  r-rcpp
)
checkdepends=(
  r-data.table
  r-dplyr
  r-fixest
  r-kit
  r-magrittr
  r-testthat
)
optdepends=(
  r-covr
  r-data.table
  r-dplyr
  r-fastverse
  r-fixest
  r-ggplot2
  r-kit
  r-knitr
  r-magrittr
  r-microbenchmark
  r-plm
  r-rcpparmadillo
  r-rcppeigen
  r-rmarkdown
  r-scales
  r-testthat
  r-tibble
  r-vars
  r-withr
  r-xts
  r-zoo
  r-bit64
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1d904fca1c30389eaf5328ec9162e86f')
b2sums=('2941e916b95993058cd6d6d63802af6c56dbdee87bce1dedae0f97700a5b5a9fd8433b990dce8cd77e836463a15ae0ab87456cde79ab8a985c035c7b52ec5d0e')

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
