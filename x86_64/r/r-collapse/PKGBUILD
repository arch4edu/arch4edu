# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=collapse
_pkgver=2.1.9
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
md5sums=('1c346d1ab6d62324aba121d113afc596')
b2sums=('fd2471f61499574de59ef72e46af3fa12886637c9eb9561f6fe76c17c617b79cee0bf96e2a7cd455528a9d4f601797e52df07efdcf1d927e8b9365cd4b8a209e')

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
