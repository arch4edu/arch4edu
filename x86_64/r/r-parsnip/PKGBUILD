# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=parsnip
_pkgver=1.7.0
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
  r-sparsevctrs
  r-tibble
  r-tidyr
  r-vctrs
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
  r-keras3
  r-kernlab
  r-kknn
  r-knitr
  r-liblinear
  r-modeldata
  r-prodlim
  r-ranger
  r-recipes
  r-remotes
  r-rmarkdown
  r-robustbase
  r-sparklyr
  r-tensorflow
  r-testthat
  r-withr
  r-workflows
  r-xgboost
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7f0a2b76de2192875cb9d1221ed0de3a')
b2sums=('f9567a013e4022f0eeaea89f987317e00a534e11078be36cdf91f788fd09fac6e35cae10f6b7cf47681f2326ee975fa04f16ec522ae2c1fa4a326cd97a4ff7c3')

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
