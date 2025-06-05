# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=collapse
_pkgver=2.1.2
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
md5sums=('affe056e257b973c5a8cdae95a5ddfa9')
b2sums=('38b716ae7b948694112a9ef72a52cf4ccdc07d434946be8f71f9c84532450bb86c3bef7effcbf350afea3af9fd61039b04ba92b65efacba77c7791f75a035234')

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
