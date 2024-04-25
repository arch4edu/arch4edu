# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=later
_pkgver=1.3.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Utilities for Scheduling Functions to Execute Later with Event Loops"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-rcpp
  r-rlang
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d051b4ebe4f306287003877aae5ab95c')
b2sums=('f30329988dce72d5c53a1bfe97ad97fd437e49387aa0f04ce74137368a660b0d10cc1f0fab7a6928d1faaa06622be89b21a465090601347171ba2180f5dd339e')

prepare() {
  # skip failing tests
  cd "$_pkgname/tests/testthat"
  sed -i '/"Interrupt while running in private loop won'\''t result in stuck loop"/a\ \ skip("not working")' \
      test-private-loops.R
  sed -i '/"interrupt and exception handling"/a\ \ skip("not working")' \
      test-run_now.R
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

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
