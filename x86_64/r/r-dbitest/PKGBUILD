# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=DBItest
_pkgver=1.8.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Testing DBI Backends"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=(LGPL)
depends=(
  r-blob
  r-callr
  r-dbi
  r-desc
  r-hms
  r-lubridate
  r-magrittr
  r-nanoarrow
  r-palmerpenguins
  r-rlang
  r-testthat
  r-vctrs
  r-withr
)
optdepends=(
  r-clipr
  r-constructive
  r-debugme
  r-devtools
  r-dplyr
  r-knitr
  r-lintr
  r-pkgload
  r-rmarkdown
  r-rsqlite
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('c30ed34e11c4e2e44ecb051fad564b66')
b2sums=('06bf87c55f921fa832f96968334932c59dcdd810eeeadeb1837ff4258cecd6c7b921053e84eb31356ea1ec7186a7b31f6e27a55da961b147f3fad352cfc68730')

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
}
