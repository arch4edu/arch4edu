# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=broom.helpers
_pkgver=1.23.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Helpers for Model Coefficients Tibbles"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r-broom
  r-cards
  r-cli
  r-dplyr
  r-labelled
  r-lifecycle
  r-purrr
  r-rlang
  r-stringr
  r-tibble
  r-tidyr
  r-tidyselect
)

optdepends=(
  r-betareg
  r-biglm
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
  r-glmtoolbox
  r-svyvgam
  r-quantreg
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('9708270005a4aa6ac22b8764d94a7b58')
b2sums=('56ab7f9fa5c2629825d3bcb6461b56b434c24be8625653a5f66029edbea0ca628ab611bf450727ac4ab526fa23696fa6b7c4a0bbc303ea9c3d0ead810ab8ea94')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
