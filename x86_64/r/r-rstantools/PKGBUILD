# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=rstantools
_pkgver=2.6.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Tools for Developing R Packages Interfacing with 'Stan'"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r-desc
  r-rcpp
  r-rcppparallel
)
checkdepends=(
  r-rstan
  r-testthat
  r-usethis
)
optdepends=(
  r-knitr
  r-pkgbuild
  r-pkgload
  r-rmarkdown
  r-roxygen2
  r-rstan
  r-rstudioapi
  r-testthat
  r-usethis
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1201be7b7001a4b5e0a9168bb275520a')
b2sums=('b8d9dec09cb803d467c773cfe44c6cfd016531475fdc6fb9259f4311f53bb699978f21075e869288a3b185bf1650aaac9b7430e2ef8155ec45da8b7893de411c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
