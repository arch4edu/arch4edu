# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ggstats
_pkgver=0.13.0
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
md5sums=('101f253bc1614f538e270a36ff0eec38')
b2sums=('e1453bddcd1abb37c1d188fbb46e50adc413a3d6a292bf65e03ed7cb57294ad449ebda5cadefbd824a4c4931d1052e0f211d1d58f2690da6880833562a9bb839')

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
