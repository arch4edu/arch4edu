# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=DT
_pkgver=0.31
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="A Wrapper of the JavaScript Library 'DataTables'"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL3)
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
md5sums=('81c595d562de4f585dd8da8a80317086')
sha256sums=('956f42a784d1c426ddc75ebfb22a854886e2d6ae8b7014b95669aed0cd699c87')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" _R_CHECK_PACKAGE_NAME_=false Rscript --vanilla test-all.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
