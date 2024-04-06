# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=broom.helpers
_pkgver=1.15.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Helpers for Model Coefficients Tibbles"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r-broom
  r-cli
  r-dplyr
  r-labelled
  r-lifecycle
  r-purrr
  r-rlang
  r-stringr
  r-tibble
  r-tidyr
)
optdepends=(
  r-betareg
  r-biglm
  r-biglmm
  r-brms
  r-broom.mixed
  r-cmprsk
  r-covr
  r-effects
  r-emmeans
  r-fixest
  r-forcats
  r-gam
  r-gee
  r-geepack
  r-ggeffects
  r-ggplot2
  r-ggstats
  r-glmmtmb
  r-glue
  r-gt
  r-gtsummary
  r-knitr
  r-lavaan
  r-lfe
  r-lme4
  r-logitr
  r-marginaleffects
  r-margins
  r-mice
  r-mmrm
  r-multgee
  r-ordinal
  r-parameters
  r-parsnip
  r-patchwork
  r-plm
  r-pscl
  r-rmarkdown
  r-rstanarm
  r-scales
  r-spelling
  r-survey
  r-testthat
  r-tidycmprsk
  r-vgam
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('19e5599a0d7734b4264d658e18f8f6d2')
b2sums=('18ce303ac7a4906f772fcc32fcfe0aea1d9962129875c48ea46ffe476df514f543d24b72a928fef4114ec867b044cc856973aea32986ba589d1e3b6cd4914358')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
