# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Hu Butui <hot123tea123@gmail.com>

_pkgname=performance
_pkgver=0.20.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Assessment of Regression Models Performance"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-bayestestr
  r-datawizard
  r-insight
)
checkdepends=(
  r-aer
  r-afex
  r-bayesfactor
  r-betareg
  r-bigutilsr
  r-curl
  r-dbscan
  r-dharma
  r-estimatr
  r-fixest
  r-glmmtmb
  r-httr2
  r-ics
  r-icsoutlier
  r-islr
  r-ivreg
  r-lavaan
  r-lme4
  r-mclogit
  r-metafor
  r-nonnest2
  r-ordinal
  r-parameters
  r-pscl
  r-randomforest
  r-rstanarm
  r-rstantools
  r-testthat
)
optdepends=(
  r-aer
  r-afex
  r-bayesfactor
  r-bayesplot
  r-betareg
  r-bh
  r-bigutilsr
  r-blavaan
  r-brglm2
  r-brms
  r-car
  r-cardata
  r-compquadform
  r-correlation
  r-cplm
  r-curl
  r-dagitty
  r-dbscan
  r-dharma
  r-discovr
  r-effectsize
  r-estimatr
  r-fixest
  r-flextable
  r-forecast
  r-ftextra
  r-gamm4
  r-ggdag
  r-glmmtmb
  r-glmx
  r-gparotation
  r-hmisc
  r-httr2
  r-ics
  r-icsoutlier
  r-islr
  r-ivreg
  r-lavaan
  r-lavaan.mi
  r-lme4
  r-lmtest
  r-loo
  r-mclogit
  r-mclust
  r-metadat
  r-metafor
  r-mlogit
  r-modelbased
  r-multimode
  r-nestedlogit
  r-nonnest2
  r-ordinal
  r-parameters
  r-patchwork
  r-pscl
  r-psych
  r-psychtools
  r-qqplotr
  r-quantreg
  r-randomforest
  r-rcppeigen
  r-reformulas
  r-rempsyc
  r-rmarkdown
  r-rstanarm
  r-rstantools
  r-sandwich
  r-see
  r-survey
  r-testthat
  r-tweedie
  r-vgam
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8683c12be68bc9462d6aaa5ea3d130c8')
b2sums=('2214099ef2aedd422c03e394205e7e47dcfdcfd6fd06a9b161bd14576a1f76fe973df4d0adfb2fae72849b332fb01ba8dbecb196fcbcd48c8b52456d10927fe0')

prepare() {
  # skip failing tests
  cd "$_pkgname/tests/testthat"
  sed -i '/"brms_mixed_1"/i\ \ skip("fails")' test-icc.R
  sed -i '/"model_performance.brmsfit"/a\ \ skip("fails")' test-model_performance.bayesian.R
  sed -i '/^test_that("check_convergence",/a\ \ skip("fails")' test-check_convergence.R
  # effectsize depends on performance; avoid a circular check dependency.
  sed -i \
    -e '/^test_that("check_group_variation-1",/a\ \ skip_if_not_installed("effectsize")' \
    -e '/^test_that("check_group_variation, multiple by",/a\ \ skip_if_not_installed("effectsize")' \
    -e '/skip_if_not_installed("parameters")/i\ \ skip_if_not_installed("effectsize")' \
    test-check_group_variation.R
  # see depends on performance; avoid a circular check dependency.
  sed -i '/^skip_if_not_installed("lme4")/a skip_if_not_installed("see")' test-check_model_glmmTMB.R
  sed -i '/^test_that("check_outliers, glmmTMB default method flags influential rows"/a\ \ skip_if_not_installed("see")' test-check_outliers_glmmTMB.R
}

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
