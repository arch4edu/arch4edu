# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=rstanarm
_pkgver=2.32.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
md5sums=('7156d76d81012785925295a8e4bdd7bc')
b2sums=('5c6e256a9066287eb600259c957c86e488cb2ce79d80a5e62404c10ab5331e21e2e93a7a49699753f4af67ec4f78cb94a2a98142ecea6fa1a4ebc36c0ad0c45f')

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

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
