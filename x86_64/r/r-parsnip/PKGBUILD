# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=parsnip
_pkgver=1.3.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="A Common API to Modeling and Analysis Functions"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-cli
  r-dplyr
  r-generics
  r-ggplot2
  r-globals
  r-glue
  r-hardhat
  r-lifecycle
  r-magrittr
  r-pillar
  r-prettyunits
  r-purrr
  r-rlang
  r-tibble
  r-tidyr
  r-vctrs
  r-withr
  r-sparsevctrs
)
checkdepends=(
  r-bench
  r-c50
  r-dials
  r-earth
  r-flexsurv
  r-keras
  r-kernlab
  r-kknn
  r-liblinear
  r-modeldata
  r-partykit
  r-ranger
  r-testthat
  r-xgboost
)
optdepends=(
  r-bench
  r-c50
  r-covr
  r-dials
  r-earth
  r-ggrepel
  r-keras
  r-kernlab
  r-kknn
  r-knitr
  r-liblinear
  r-modeldata
  r-prodlim
  r-ranger
  r-remotes
  r-rmarkdown
  r-sparklyr
  r-tensorflow
  r-testthat
  r-xgboost
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('5561028fb18dff96abf0e781666e8812')
b2sums=('9eb0894bd72f401a221ceac7b78c3b4c85891b9516461205920961bbc380c8562dd9c4eee7a86f781af9aa35a2dc6885e5fd307d1f43b69a80a167ade44f6c68')

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
