# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ggstats
_pkgver=0.6.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Extension to 'ggplot2' for Plotting Stats"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r-broom.helpers
  r-cli
  r-dplyr
  r-forcats
  r-ggplot2
  r-lifecycle
  r-magrittr
  r-patchwork
  r-purrr
  r-rlang
  r-scales
  r-stringr
  r-tidyr
)
checkdepends=(
  r-betareg
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
  r-emmeans
  r-glue
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
md5sums=('6e82ffaa172a83d3063bb7e30c40da41')
b2sums=('fe087398fcae03ac7fefb2b04dd3ab1eb7a4df34b7b84b21fc4e35209da6408bc54e5c8c2ec6ae8dc726aff93e952d8ebc5d10844da1636dc4caa88643fbea0d')

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
