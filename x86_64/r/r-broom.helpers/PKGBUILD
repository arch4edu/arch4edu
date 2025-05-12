# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=broom.helpers
_pkgver=1.21.0
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
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('450c12c4d0db7be693cb5c505a74c189')
b2sums=('f1bfb114dc2b62ed1b192b6c73719563f87b28444bc06ecf7499f92bc004c70a1a7fee5733d01f3bcafc2edc83b3a3b71e68830e87206bdda6b0a44754d7f5b5')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
