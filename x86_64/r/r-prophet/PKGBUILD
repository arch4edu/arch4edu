# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=prophet
_pkgver=1.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=8
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
  r-knitr
  r-readr
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8df583834d8cb58ebc4cd5421497d9dd')
b2sums=('0d32ae2bac0ab2257643c2da03ae9372338f33b60e26f5a6d021de87214c9222481cb80517602d1c798a9de268ccb904daf5a6f8d53d2680c679e03866022a34')

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
