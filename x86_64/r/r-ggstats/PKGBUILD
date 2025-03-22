# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ggstats
_pkgver=0.9.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Extension to 'ggplot2' for Plotting Stats"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r-cli
  r-dplyr
  r-forcats
  r-ggplot2
  r-lifecycle
  r-patchwork
  r-purrr
  r-rlang
  r-scales
  r-stringr
  r-tidyr
)
checkdepends=(
  r-betareg
  r-broom
  r-broom.helpers
  r-emmeans
  r-parameters
  r-pscl
  r-reshape
  r-survey
  r-testthat
  r-vdiffr
)
optdepends=(
  r-betareg
  r-broom
  r-broom.helpers
  r-emmeans
  r-glue
  r-gtsummary
  r-knitr
  r-labelled
  r-parameters
  r-pscl
  r-reshape
  r-rmarkdown
  r-spelling
  r-survey
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('574df8d8ca1126f79652d4c8b889fd91')
b2sums=('f86023cd9409fb4aeda234da4176fb32cdb72b26115b48db3598898bab2c27b09f415cad569c000d16a5750a371c6e01ef21d687fad0e1d4d2b6368b25f8d4a5')

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
