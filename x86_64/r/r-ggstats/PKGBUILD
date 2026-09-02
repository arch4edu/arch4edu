# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ggstats
_pkgver=0.14.0
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
md5sums=('100b331e3f2c7b4a3d8bd4a490d0db5e')
b2sums=('9a922f874c21d7eebdc544ddb3d081ed305aa01385a4d634ddcde9fed7987a7d43cec43eb7c2dfc903b14cd1a36913e933e2eaeab62e6ee2b7b4e3a05aea52ad')

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
