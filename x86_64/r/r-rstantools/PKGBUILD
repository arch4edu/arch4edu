# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=rstantools
_pkgver=2.7.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Tools for Developing R Packages Interfacing with 'Stan'"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r-desc
  r-quickjsr
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
md5sums=('844467ff2ad80062af632197652b1d6d')
b2sums=('f69dde9fe27735949fa41ee50e71b44bd2a09bfd49174109b79719570b1ab4ec934f13bd1ff3a5ab6cd828f3b3df8cb4dad6b86194b4d8cab421065b699a6bd6')

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
