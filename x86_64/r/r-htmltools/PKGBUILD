# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=htmltools
_pkgver=0.5.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=3
pkgdesc="Tools for HTML"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
depends=(
  r-base64enc
  r-digest
  r-ellipsis
  r-fastmap
  r-rlang
)
checkdepends=(
  r-markdown
  r-testthat
)
optdepends=(
  r-cairo
  r-markdown
  r-ragg
  r-shiny
  r-testthat
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('27fa1c4bebbd27ab12b3277309a13aca')
sha256sums=('c8b23fab855a89c6ed0f6d6c7cad0ff9c5ae329c0bdb479940443ee752f26659')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla test-all.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
