# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=DBItest
_pkgver=1.7.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Testing DBI Backends"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(LGPL)
depends=(
  r-blob
  r-callr
  r-dbi
  r-desc
  r-hms
  r-lubridate
  r-palmerpenguins
  r-r6
  r-rlang
  r-testthat
  r-vctrs
  r-withr
)
optdepends=(
  r-clipr
  r-dblog
  r-debugme
  r-devtools
  r-knitr
  r-lintr
  r-rmarkdown
  r-rsqlite
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a43445d47911fa2d62ec63c653522354')
sha256sums=('30b7026378fedaec7e730fa4e242968dd70642f496457d7bf47d35e5c7ab891c')

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
}
