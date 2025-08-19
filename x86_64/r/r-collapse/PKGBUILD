# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=collapse
_pkgver=2.1.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Advanced and Fast Data Transformation"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later AND MPL-2.0')
depends=(
  r-rcpp
)
checkdepends=(
  r-data.table
  r-dplyr
  r-fixest
  r-kit
  r-magrittr
  r-testthat
)
optdepends=(
  r-covr
  r-data.table
  r-dplyr
  r-fastverse
  r-fixest
  r-ggplot2
  r-kit
  r-knitr
  r-magrittr
  r-microbenchmark
  r-plm
  r-rcpparmadillo
  r-rcppeigen
  r-rmarkdown
  r-scales
  r-testthat
  r-tibble
  r-vars
  r-withr
  r-xts
  r-zoo
  r-bit64
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f4b45c16e1a736a8036b341001fb4b7d')
b2sums=('2449fe54d2ba13f7d510af965e40c0570db82db977d8aad0a20e3e5a78c2a77cd5e1a32181e1560c240268e08df1de402fb9b36cd374860f8103954d6c67cf3f')

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
