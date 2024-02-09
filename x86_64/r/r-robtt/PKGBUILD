# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=RoBTT
_pkgver=1.2.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
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
md5sums=('50e0eea609a0aae0eb0cce7451076fd9')
b2sums=('27018211f78ffdfc4f028e66168ec3af6aef3601614c0f3b372796ca1890bffe6e6044d1ddd165d2eaccbcd066086f6a05c65ff337f06d7b8ee6e02ea6b2f8a4')

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
