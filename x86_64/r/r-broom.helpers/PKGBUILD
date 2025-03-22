# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=broom.helpers
_pkgver=1.20.0
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
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('35765a7529de9eed8db66f495f9aa344')
b2sums=('9710c6d585cef46103a0a40dc67624e188f4e5dfdf8d11de52e3f921fcd7da00f18d1d7eb10131bfcde348332af14b6b6c32c0277ab110f938b611ac3a3df16e')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
