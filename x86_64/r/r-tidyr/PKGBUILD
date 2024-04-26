# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_pkgname=tidyr
_pkgver=1.3.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Tidy Messy Data"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-cli
  r-dplyr
  r-glue
  r-lifecycle
  r-magrittr
  r-purrr
  r-rlang
  r-stringr
  r-tibble
  r-tidyselect
  r-vctrs
)
makedepends=(
  r-cpp11
)
checkdepends=(
  r-data.table
  r-testthat
)
optdepends=(
  r-covr
  r-data.table
  r-knitr
  r-readr
  r-repurrrsive
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "fix-tests.patch")
md5sums=('0491d9d3359af7baf8ad9003ce44aa1d'
         'c59cb36104f4ba2550cadc60b9af427e')
b2sums=('43ec7fca79d137205847ae837a20f6ed2be8d4440cde29f6ff11cac0df35a1fbdb6d55d1365303819d25f5333819c9541a4e0a006e39e22cfa665c0f9d8fbf76'
        '7567abe193a23f244e760e8eefc45af2438d3754fd4f628d2b5ddb9113a8f67bdd870acb8232a13504e97b807bd210195b4516d3e3c76e1a396496f8b1edf01c')

prepare() {
  # fix outdated snapshot tests
  patch -Np1 -i fix-tests.patch
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
