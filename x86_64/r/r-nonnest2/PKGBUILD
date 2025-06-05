# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=nonnest2
_pkgver=0.5-8
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Tests of Non-Nested Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only OR GPL-3.0-only')
depends=(
  r-compquadform
  r-lavaan
  r-mvtnorm
  r-sandwich
)
checkdepends=(
  r-aer
  r-faraway
  r-mlogit
  r-openmx
  r-ordinal
  r-pscl
  r-testthat
)
optdepends=(
  r-aer
  r-faraway
  r-knitr
  r-mirt
  r-mlogit
  r-openmx
  r-ordinal
  r-pscl
  r-rmarkdown
  r-testthat
  r-tidysem
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7cdabf2deb5e63a1733b8e0b2a84b898')
b2sums=('dc48b7ae6391ae0beef946715a232bf5a4de5de9b62bd368937c02a836f1821a85bb71cf788b67503746d0734821a7a53028fd80fc41a3bf895bbabb9e6e24b5')

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
