# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=DT
_pkgver=0.32
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
md5sums=('e43c80e1b807de68609808b62971034c')
b2sums=('d157a5ce07e1a8e01dfc98e5a29c79726df0ae3ef734192f9c5b77a951d9ed9d9e43fdfcd9da6ab09632824637b34ca61a813219d5569d37e51ecdc0d9b91f3e')

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
