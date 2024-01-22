# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=DT
_pkgver=0.31
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
md5sums=('81c595d562de4f585dd8da8a80317086')
b2sums=('2d1595490aa901bc4b462b41cc805a3d1dfe53ec34af44f08a62b62f176be41371f3b41de87d7f8e6ef8ab8bd7d5bffd4330e8d15d60ea0d28a3aefb5949e17e')

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
