# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=rstanarm
_pkgver=2.32.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Bayesian Applied Regression Modeling via Stan"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  onetbb
  pandoc
  r-bayesplot
  r-ggplot2
  r-lme4
  r-loo
  r-posterior
  r-rcpp
  r-rcppparallel
  r-reformulas
  r-rstan
  r-rstantools
  r-shinystan
)
makedepends=(
  r-bh
  r-rcppeigen
  r-stanheaders
)
checkdepends=(
  r-betareg
  r-biglm
  r-data.table
  r-hsaur3
  r-testthat
)
optdepends=(
  r-betareg
  r-biglm
  r-data.table
  r-digest
  r-gamm4
  r-gridextra
  r-hsaur3
  r-knitr
  r-rmarkdown
  r-roxygen2
  r-shiny
  r-stanheaders
  r-testthat
  r-v8
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('82427d710596d42b0c9e4488981b7d38')
b2sums=('a6577a28383d6332ccd22b6aec0f76d6a8690eeac8d260579647a3651f47c150a778b08c7bdf2d18ba43d8ed6f13cbe72bc7fde711bc70df26cf3cb48d97eb72')

prepare() {
  cd "$_pkgname/tests/testthat"
  # skip tests that make a coredump
  sed -e '/"stan_betareg ok when modeling x and z (link.phi = '\'sqrt\'')"/a\ \ skip("dumps core")' \
      -e '/"heavy tailed priors work with stan_betareg"/a\ \ skip("dumps core")' \
      -i test_stan_betareg.R
  sed -i '1i skip("dumps core")' test_stan_jm.R
  sed -i '/"multiple grouping factors are ok"/a\ \ skip("dumps core")' test_stan_mvmer.R
}

build() {
  mkdir build
  # compilation needs a lot of memory
  MAKEFLAGS+=" -j1"
  R CMD INSTALL -l build "$_pkgname"
}

# check() {
#   cd "$_pkgname/tests"
#   R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
# }

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
