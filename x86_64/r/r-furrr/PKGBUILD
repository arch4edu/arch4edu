# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=furrr
_pkgver=0.3.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=7
pkgdesc="Apply Mapping Functions in Parallel using Futures"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
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
b2sums=('aabe78f39b22e14ae8d539c867ccb8ab4588ff57f7854ea5e69b5846876eeea7d7fbfdfc68ad66871548cf12999a32173ec9fbd966cfc20e8ec5b9cc0c307cd4')

prepare() {
  # fix snapshot test
  sed -i 's/Please use/i Please use/' "$_pkgname/tests/testthat/_snaps/deprecation.md"
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
