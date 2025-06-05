# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=glmmTMB
_pkgver=1.1.11
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
  r-reformulas
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
md5sums=('bc7f6ddc011bfc03f2bdb6dfb1cf4230')
b2sums=('42a52bd00af5ea1321c97372c44441cf6a62b96aefff7f3507bcce2e0637bd89033d9e936b4ca8d9e4921d29c7b78c9bd90a0708c70a530b90ee561bfbbc1093')

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
