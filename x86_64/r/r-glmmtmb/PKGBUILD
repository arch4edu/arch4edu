# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=glmmTMB
_pkgver=1.1.15.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Generalized Linear Mixed Models using Template Model Builder"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('AGPL-3.0-only')
depends=(
  r-lme4
  r-numderiv
  r-pbkrtest
  r-reformulas
  r-rtmb
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
  r-ordinal
  r-plyr
  r-png
  r-pscl
  r-purrr
  r-reshape2
  r-rmarkdown
  r-testthat
  r-texreg
  r-withr
  r-xtable
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('6e71df854fdceb4e1ef9facb931fe442')
b2sums=('0f4727256c83da1c01aef6e2c5e562b7eeafab9a54990276515ce471cd1e3304e14983439176fc43172951130f8694e36ef62e800c16a9ede459e99020c93efc')

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
