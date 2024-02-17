# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=parsnip
_pkgver=1.2.0
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
)
checkdepends=(
  python-tensorflow
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
  r-tensorflow
  r-testthat
  r-xgboost
)
optdepends=(
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
md5sums=('5511bd877b251ff068613fd7e47d387c')
b2sums=('2824147e2f4c46329ab4575f9a4493cc68d141ec031271799e5874a5b4e4148842db38d638b567ed4091e1f9fbe05e371a828c00f2fb603c6d6506c8d07c4181')

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
