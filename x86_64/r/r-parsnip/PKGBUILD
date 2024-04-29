# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=parsnip
_pkgver=1.2.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
md5sums=('8963904d37b6296869d29d0a8c22e61a')
b2sums=('b4456b926bbcb92b68a442c155e954d585c7695dd2e65b6ee2c2351ddb4e4e63b2896ec223c8b20ae62903a90778f16a28b97e7437820fdb37b5efa0c9f6643d')

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
