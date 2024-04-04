# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=DT
_pkgver=0.33
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="A Wrapper of the JavaScript Library 'DataTables'"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only AND MIT AND Apache-2.0')
depends=(
  r-crosstalk
  r-htmltools
  r-htmlwidgets
  r-httpuv
  r-jquerylib
  r-jsonlite
  r-magrittr
  r-promises
)
checkdepends=(
  r-testit
)
optdepends=(
  r-bslib
  r-future
  r-knitr
  r-rmarkdown
  r-shiny
  r-testit
  r-tibble
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('360d1d38b0f28485d564bb246a27c1f2')
b2sums=('b9fa2c7c3e6960ea4ba638ed5029397e428c53422eef9b6a17a5a20b184c26a1665fa9d973c4c31b050130189b2714a4aa0f72d55b6f874dbea022fa7555e452')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" _R_CHECK_PACKAGE_NAME_=false Rscript --vanilla test-all.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
