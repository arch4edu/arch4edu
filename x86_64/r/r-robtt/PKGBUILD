# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=RoBTT
_pkgver=1.3.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Robust Bayesian T-Test"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  onetbb
  r-bayestools
  r-bridgesampling
  r-ggplot2
  r-rcpp
  r-rcppparallel
  r-rdpack
  r-rstan
  r-rstantools
)
makedepends=(
  r-bh
  r-rcppeigen
  r-stanheaders
)
checkdepends=(
  r-testthat
  r-vdiffr
)
optdepends=(
  r-covr
  r-knitr
  r-rmarkdown
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('aa8b805fa470d5bb0845eec1cf08ddf8')
b2sums=('0e79d62fc434d8f42860e68f7da2783b28c6cfc46efc3a112fa5d2687332d340f76b66f63155d276715ac857b5941b05d916b65e80212e439da17ddaac982250')

prepare() {
  # skip test that requires external files
  sed -i '1a skip("Requires external files")' \
      "$_pkgname/tests/testthat/test-4-diagnostics.R"
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
