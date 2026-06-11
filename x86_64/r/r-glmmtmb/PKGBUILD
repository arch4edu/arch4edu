# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=glmmTMB
_pkgver=1.1.14
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Generalized Linear Mixed Models using Template Model Builder"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('AGPL-3.0-only')
depends=(
  r-lme4
  r-numderiv
  r-pbkrtest
  r-reformulas
  r-sandwich
  r-tmb
)
makedepends=(
  r-rcppeigen
)
checkdepends=(
  r-ade4
  r-ape
  r-car
  r-effects
  r-emmeans
  r-pscl
  r-sandwich
  r-testthat
)
optdepends=(
  r-ade4
  r-ape
  r-bbmle
  r-blme
  r-broom
  r-broom.mixed
  r-car
  r-coda
  r-dharma
  r-dotwhisker
  r-dplyr
  r-effects
  r-emmeans
  r-estimability
  r-ggplot2
  r-gsl
  r-huxtable
  r-knitr
  r-lmertest
  r-metafor
  r-mlmrev
  r-multcomp
  r-mumin
  r-plyr
  r-png
  r-pscl
  r-purrr
  r-reshape2
  r-rmarkdown
  r-testthat
  r-texreg
  r-xtable
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('adfb0befff58ba57647c796498adc0d0')
b2sums=('18f70f641fbf76b9505df75b06d3d672935b427dff90f28b77a771ce52890a93bdb50ece44345dca0471ab05f23acf711974225ead2d4c50ef4124249f443d11')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

#check() {
#  cd "$_pkgname/tests"
#  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla AAAtest-all.R
#}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
