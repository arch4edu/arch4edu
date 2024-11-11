# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=RoBTT
_pkgver=1.3.1
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
md5sums=('cf5a7ebd9eabf9b2c1e754dc901991be')
b2sums=('92e684d87027aa735bbf2d150bf9acd1c6bcf9152d7cd26b23ba355c4be34cee8099a274dbe891267047a9106e7ef5fdb7e3ceabdc5aacedde5ecf7cb4b83e6b')

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
