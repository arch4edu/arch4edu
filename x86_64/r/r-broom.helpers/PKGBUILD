# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=broom.helpers
_pkgver=1.16.0
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
md5sums=('b723f96d34c9155ed7fc97b134608c99')
b2sums=('83fd12afa572346dc2af0444f957a6c3d86d4d5649e8a1254723d233b378934d19734d6f71298e627301b91f8db6472a5e0741d88c2acd632a2543e578db87f7')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
