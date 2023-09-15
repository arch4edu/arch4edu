# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=rstanarm
_pkgver=2.26.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Bayesian Applied Regression Modeling via Stan"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL3)
depends=(
  pandoc
  r-bayesplot
  r-ggplot2
  r-lme4
  r-loo
  r-posterior
  r-rcpp
  r-rcppparallel
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
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8505a33ae9ff139e9f0b3d5b8cc6ee7e')
sha256sums=('4a54792d6e035931b613647aebfc98b81d1aac646a5a3f6f116b6f560d544444')

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
  mkdir -p build
  # compilation needs a lot of memory
  MAKEFLAGS+=" -j1"
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
