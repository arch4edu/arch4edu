# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=rstantools
_pkgver=2.4.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
md5sums=('abd80e8b316191cb4e146e09ee9c06fd')
b2sums=('3474c564f13f0421321033f919a5e2065b407a7fb5a0d65c96c4a99a311ead29f0798041ec9e1b99ebe11053b4b6876e97a62578e65410b3eea3344e5e119c02')

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
