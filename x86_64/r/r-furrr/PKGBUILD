# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=furrr
_pkgver=0.3.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=6
pkgdesc="Apply Mapping Functions in Parallel using Futures"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
depends=(
  r-future
  r-globals
  r-lifecycle
  r-purrr
  r-rlang
  r-vctrs
)
checkdepends=(
  r-dplyr
  r-testthat
)
optdepends=(
  r-carrier
  r-covr
  r-dplyr
  r-knitr
  r-listenv
  r-magrittr
  r-rmarkdown
  r-testthat
  r-tidyselect
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('813dfb60e455c5667be5117b3df2943b')
sha256sums=('0d91735e2e9be759b1ab148d115c2c7429b79740514778828e5dab631dc0e48b')

prepare() {
  # fix snapshot test
  sed -i 's/Please use/i Please use/' "$_pkgname/tests/testthat/_snaps/deprecation.md"
}

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
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
