# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=furrr
_pkgver=0.4.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Apply Mapping Functions in Parallel using Futures"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-future
  r-globals
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
  r-testthat
  r-tidyselect
  r-parallelly
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a18b1988e46dd7fd96c94272699d1a70')
b2sums=('e8775756d97adb4a2bfe083e3e5788fb4e667f5335333570e8693585c91429879b2a2334ec9780d160f2033c652b91350665439ebaa386a9052abce4720adcf0')

#prepare() {
  # fix snapshot test
#  sed -i 's/Please use/i Please use/' "$_pkgname/tests/testthat/_snaps/deprecation.md"
#}

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

_check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
