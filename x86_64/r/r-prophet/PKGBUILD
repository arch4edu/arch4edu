# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=prophet
_pkgver=1.1.7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Automatic Forecasting Procedure"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  onetbb
  r-dplyr
  r-dygraphs
  r-extradistr
  r-ggplot2
  r-lubridate
  r-rcpp
  r-rcppparallel
  r-rlang
  r-rstan
  r-rstantools
  r-scales
  r-stanheaders
  r-tidyr
  r-xts
)
makedepends=(
  r-bh
  r-rcppeigen
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-cmdstanr
  r-knitr
  r-posterior
  r-readr
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f3c44b3b6780dfe3b4c9d5652732e700')
b2sums=('5a24b31a21c517a59e5916cb3eb3b58bce9fc40333af6bc7cc88202042acf2565b094053e514dd03c0ee2bed15b5dcd070ee1b51e718d703abfdd43707c6e894')

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
